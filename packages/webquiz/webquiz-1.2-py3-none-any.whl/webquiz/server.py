import asyncio
import json
import csv
import uuid
import yaml
import os
import sys
import socket
import subprocess
import platform
import zipfile
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from aiohttp import web, WSMsgType, ClientSession
import aiofiles
import logging
from io import StringIO
from dataclasses import dataclass, asdict

from webquiz import __version__ as package_version

# Logger will be configured in create_app() with custom log file
logger = logging.getLogger(__name__)

def read_package_resource(filename: str) -> str:
    """Read a file from the webquiz package resources"""
    try:
        # Try modern importlib.resources first (Python 3.9+)
        import importlib.resources as pkg_resources
        return (pkg_resources.files('webquiz') / filename).read_text(encoding='utf-8')
    except (ImportError, AttributeError):
        # Fallback to pkg_resources for older Python versions
        import pkg_resources
        return pkg_resources.resource_string('webquiz', filename).decode('utf-8')

def get_package_version() -> str:
    """Get the webquiz package version"""
    try:
        return package_version
    except Exception:
        return 'unknown'

def resolve_path_relative_to_binary(path_str: str) -> str:
    """Resolve relative paths relative to binary directory when running as binary."""
    if not path_str or os.path.isabs(path_str):
        return path_str
    
    binary_dir = os.environ.get('WEBQUIZ_BINARY_DIR')
    if binary_dir:
        # Running as binary - resolve relative to binary directory
        resolved = Path(binary_dir) / path_str
        return str(resolved)
    else:
        # Running normally - return as-is (relative to cwd)
        return path_str

@dataclass
class ServerConfig:
    """Server configuration data class"""
    host: str = "0.0.0.0"
    port: int = 8080

@dataclass  
class PathsConfig:
    """Paths configuration data class"""
    quizzes_dir: str = None
    logs_dir: str = None
    csv_dir: str = None
    static_dir: str = None
    
    def __post_init__(self):
        if self.quizzes_dir is None:
            self.quizzes_dir = resolve_path_relative_to_binary("quizzes")
        if self.logs_dir is None:
            self.logs_dir = resolve_path_relative_to_binary("logs")
        if self.csv_dir is None:
            self.csv_dir = resolve_path_relative_to_binary("data")
        if self.static_dir is None:
            self.static_dir = resolve_path_relative_to_binary("static")

@dataclass
class AdminConfig:
    """Admin configuration data class"""
    master_key: Optional[str] = None
    trusted_ips: List[str] = None
    
    def __post_init__(self):
        if self.trusted_ips is None:
            self.trusted_ips = ['127.0.0.1']

@dataclass
class OptionsConfig:
    """Options configuration data class"""
    flush_interval: int = 30

@dataclass
class DownloadableQuiz:
    """Downloadable quiz configuration"""
    name: str
    download_path: str
    folder: str

@dataclass
class QuizzesConfig:
    """Downloadable quizzes configuration data class"""
    quizzes: List[DownloadableQuiz] = None
    
    def __post_init__(self):
        if self.quizzes is None:
            self.quizzes = []

@dataclass
class WebQuizConfig:
    """Main configuration data class"""
    server: ServerConfig = None
    paths: PathsConfig = None
    admin: AdminConfig = None
    options: OptionsConfig = None
    quizzes: QuizzesConfig = None
    
    def __post_init__(self):
        if self.server is None:
            self.server = ServerConfig()
        if self.paths is None:
            self.paths = PathsConfig()
        if self.admin is None:
            self.admin = AdminConfig()
        if self.options is None:
            self.options = OptionsConfig()
        if self.quizzes is None:
            self.quizzes = QuizzesConfig()

def ensure_directory_exists(path: str) -> str:
    """Create directory if it doesn't exist and return the path"""
    os.makedirs(path, exist_ok=True)
    return path

def load_config_from_yaml(config_path: str) -> WebQuizConfig:
    """Load configuration from YAML file"""
    try:
        with open(config_path, 'r') as f:
            config_data = yaml.safe_load(f)
        
        if not config_data:
            return WebQuizConfig()
            
        # Create config objects from YAML data
        server_config = ServerConfig(**(config_data.get('server', {})))
        paths_config = PathsConfig(**(config_data.get('paths', {})))
        admin_config = AdminConfig(**(config_data.get('admin', {})))
        options_config = OptionsConfig(**(config_data.get('options', {})))
        
        # Parse downloadable quizzes configuration
        quizzes_data = config_data.get('quizzes', [])
        downloadable_quizzes = []
        if quizzes_data:
            for quiz_data in quizzes_data:
                downloadable_quizzes.append(DownloadableQuiz(
                    name=quiz_data['name'],
                    download_path=quiz_data['download_path'],
                    folder=quiz_data['folder']
                ))
        quizzes_config = QuizzesConfig(quizzes=downloadable_quizzes)
        
        return WebQuizConfig(
            server=server_config,
            paths=paths_config,
            admin=admin_config,
            options=options_config,
            quizzes=quizzes_config
        )
    except FileNotFoundError:
        logger.warning(f"Config file not found: {config_path}, using defaults")
        return WebQuizConfig()
    except Exception as e:
        logger.error(f"Error loading config from {config_path}: {e}")
        return WebQuizConfig()

def get_default_config_path() -> Optional[str]:
    """Get default config file path, creating one if it doesn't exist."""
    # Determine where to look for/create config file
    binary_dir = os.environ.get('WEBQUIZ_BINARY_DIR')
    if binary_dir:
        config_path = Path(binary_dir) / "webquiz.yaml"
    else:
        config_path = Path.cwd() / "webquiz.yaml"
    
    # If config file exists, return it
    if config_path.exists():
        return str(config_path)
    
    # Create default config file
    try:
        create_default_config_file(config_path)
        return str(config_path)
    except Exception as e:
        logger.warning(f"Could not create default config file at {config_path}: {e}")
        return None

def create_default_config_file(config_path: Path):
    """Create a default config file with example content."""
    example_content = read_package_resource('server_config.yaml.example')

    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(example_content)
    logger.info(f"Created default config file: {config_path}")

def load_config_with_overrides(config_path: Optional[str] = None, **cli_overrides) -> WebQuizConfig:
    """Load configuration with CLI parameter overrides
    
    Priority: CLI parameters > config file > defaults
    """
    # Use default config file if none provided
    if not config_path:
        config_path = get_default_config_path()
    
    # Start with config file or defaults
    if config_path:
        if os.path.exists(config_path):
            config = load_config_from_yaml(config_path)
            logger.info(f"Loaded configuration from: {config_path}")
        else:
            # Config file specified but doesn't exist - create from example
            create_default_config_file(Path(config_path))
            config = load_config_from_yaml(config_path)
            logger.info(f"Loaded configuration from newly created: {config_path}")
    else:
        config = WebQuizConfig()
        logger.info("Using default configuration")
    
    # Apply CLI overrides
    for key, value in cli_overrides.items():
        if value is not None:  # Only override if CLI parameter was provided
            if key in ['host', 'port']:
                setattr(config.server, key, value)
            elif key in ['quizzes_dir', 'logs_dir', 'csv_dir', 'static_dir']:
                setattr(config.paths, key, value)
            elif key in ['master_key']:
                setattr(config.admin, key, value)
            elif key in ['flush_interval']:
                setattr(config.options, key, value)
    
    # Environment variable override for master key
    env_master_key = os.environ.get('WEBQUIZ_MASTER_KEY')
    if env_master_key and not cli_overrides.get('master_key'):
        config.admin.master_key = env_master_key
        logger.info("Master key loaded from environment variable")
    
    return config

def generate_unique_filename(base_path: str) -> str:
    """Generate a unique filename with suffix (0001, 0002, etc.) if file exists"""
    if not os.path.exists(base_path):
        return base_path
    
    # Split the path into name and extension
    name, ext = os.path.splitext(base_path)
    
    # Find the next available suffix
    suffix = 1
    while True:
        new_path = f"{name}_{suffix:04d}{ext}"
        if not os.path.exists(new_path):
            return new_path
        suffix += 1

def get_client_ip(request):
    """Extract client IP address from request, handling proxies"""
    client_ip = request.remote or '127.0.0.1'
    if 'X-Forwarded-For' in request.headers:
        # Handle proxy/load balancer forwarded IPs (take the first one)
        client_ip = request.headers['X-Forwarded-For'].split(',')[0].strip()
    elif 'X-Real-IP' in request.headers:
        client_ip = request.headers['X-Real-IP']
    return client_ip

def get_network_interfaces():
    """Get all network interfaces and their IP addresses"""
    interfaces = []
    try:
        # Get hostname
        hostname = socket.gethostname()
        
        # Get all IP addresses associated with the hostname
        ip_addresses = socket.getaddrinfo(hostname, None, socket.AF_INET)
        for ip_info in ip_addresses:
            ip = ip_info[4][0]
            if ip != '127.0.0.1':  # Skip localhost
                interfaces.append(ip)
        
        # Also try to get more interface info on Unix systems
        if platform.system() != 'Windows':
            try:
                result = subprocess.run(['hostname', '-I'], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    ips = result.stdout.strip().split()
                    for ip in ips:
                        if ip not in interfaces and ip != '127.0.0.1':
                            interfaces.append(ip)
            except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
                pass
    except Exception:
        pass
    
    return list(set(interfaces))  # Remove duplicates

def get_wifi_name():
    """Get the current WiFi network name"""
    try:
        system = platform.system()
        
        if system == 'Darwin':  # macOS
            result = subprocess.run(
                ['networksetup', '-getairportnetwork', 'en0'], 
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                output = result.stdout.strip()
                if 'Current Wi-Fi Network:' in output:
                    return output.split('Current Wi-Fi Network:')[1].strip()
        
        elif system == 'Linux':
            # Try multiple methods for Linux
            commands = [
                ['iwgetid', '-r'],
                ['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'],
            ]
            
            for cmd in commands:
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        output = result.stdout.strip()
                        if output:
                            # For nmcli, filter active connections
                            if 'nmcli' in cmd:
                                lines = output.split('\n')
                                for line in lines:
                                    if line.startswith('yes:'):
                                        return line.split(':', 1)[1]
                            else:
                                return output
                except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
                    continue
        
        elif system == 'Windows':
            result = subprocess.run(
                ['netsh', 'wlan', 'show', 'profiles'], 
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'All User Profile' in line and '*' in line:
                        return line.split(':')[1].strip()
    
    except Exception:
        pass
    
    return 'Unknown'

def admin_auth_required(func):
    """Decorator to require master key authentication for admin endpoints"""
    async def wrapper(self, request):
        # Check if master key is provided
        if not self.master_key:
            return web.json_response({'error': 'Admin functionality disabled - no master key set'}, status=403)
        
        # Get client IP and check if it's in trusted list (bypass authentication)
        client_ip = get_client_ip(request)
        if hasattr(self, 'admin_config') and client_ip in self.admin_config.trusted_ips:
            return await func(self, request)
        
        # Get master key from request (header or body)
        provided_key = request.headers.get('X-Master-Key')
        if not provided_key:
            try:
                data = await request.json()
                provided_key = data.get('master_key')
            except:
                pass
        
        if not provided_key or provided_key != self.master_key:
            return web.json_response({'error': 'Недійсний або відсутній головний ключ'}, status=401)
        
        return await func(self, request)
    return wrapper

@web.middleware
async def error_middleware(request, handler):
    """Global error handling middleware"""
    try:
        return await handler(request)
    except web.HTTPException:
        raise
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return web.json_response({'error': str(e)}, status=400)


class TestingServer:
    def __init__(self, config: WebQuizConfig):
        self.config = config
        self.quizzes_dir = config.paths.quizzes_dir
        self.master_key = config.admin.master_key
        self.admin_config = config.admin  # Store admin config for IP whitelist access
        self.current_quiz_file = None  # Will be set when quiz is selected
        self.logs_dir = config.paths.logs_dir
        self.csv_dir = config.paths.csv_dir
        self.static_dir = config.paths.static_dir
        self.log_file = None  # Will be set during initialization
        self.csv_file = None  # Will be set when quiz is selected
        self.quiz_title = 'Система Тестування'  # Default title, updated when quiz is loaded
        self.show_right_answer = True  # Default setting, updated when quiz is loaded
        self.users: Dict[str, Dict[str, Any]] = {}  # user_id -> user data
        self.questions: List[Dict[str, Any]] = []
        self.user_responses: List[Dict[str, Any]] = []
        self.user_progress: Dict[str, int] = {}  # user_id -> last_answered_question_id
        self.question_start_times: Dict[str, datetime] = {}  # user_id -> question_start_time
        self.user_stats: Dict[str, Dict[str, Any]] = {}  # user_id -> final stats for completed users
        self.user_answers: Dict[str, List[Dict[str, Any]]] = {}  # user_id -> list of answers for stats calculation
        
        # Live stats WebSocket infrastructure
        self.websocket_clients: List[web.WebSocketResponse] = []  # Connected WebSocket clients
        self.live_stats: Dict[str, Dict[int, str]] = {}  # user_id -> {question_id: state}

        # Preload templates
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, str]:
        """Preload all templates at startup"""
        templates = {}
        template_files = [
            'index.html',
            'admin.html',
            'files.html',
            'live_stats.html',
            'quiz_selection_required.html',
            'template_error.html'
        ]

        for template_file in template_files:
            try:
                templates[template_file] = read_package_resource(f'templates/{template_file}')
                logger.info(f"Loaded template: {template_file}")
            except Exception as e:
                logger.warning(f"Failed to load template {template_file}: {e}")

        return templates

    def generate_log_path(self) -> str:
        """Generate log file path in logs directory with simple numeric naming"""
        ensure_directory_exists(self.logs_dir)
        
        # Find the next available number
        suffix = 1
        while True:
            log_path = os.path.join(self.logs_dir, f"{suffix:04d}.log")
            if not os.path.exists(log_path):
                return log_path
            suffix += 1
        
    def generate_csv_path(self, quiz_name: str) -> str:
        """Generate CSV file path in CSV directory with quiz name and numeric naming"""
        ensure_directory_exists(self.csv_dir)
        
        # Clean quiz name (remove extension)
        quiz_prefix = quiz_name.replace('.yaml', '').replace('.yml', '')
        
        # Find the next available number for this quiz
        suffix = 1
        while True:
            csv_path = os.path.join(self.csv_dir, f"{quiz_prefix}_{suffix:04d}.csv")
            if not os.path.exists(csv_path):
                return csv_path
            suffix += 1
        
    def reset_server_state(self):
        """Reset all server state for new quiz"""
        self.users.clear()
        self.user_responses.clear()
        self.user_progress.clear()
        self.question_start_times.clear()
        self.user_stats.clear()
        self.user_answers.clear()
        self.live_stats.clear()
        logger.info("Server state reset for new quiz")
        
    async def list_available_quizzes(self):
        """List all available quiz files in quizzes directory"""
        try:
            quiz_files = []
            if os.path.exists(self.quizzes_dir):
                for filename in os.listdir(self.quizzes_dir):
                    if filename.endswith(('.yaml', '.yml')):
                        quiz_files.append(filename)
            return sorted(quiz_files)
        except Exception as e:
            logger.error(f"Error listing quiz files: {e}")
            return []
            
    async def switch_quiz(self, quiz_filename: str):
        """Switch to a different quiz file and reset server state"""
        quiz_path = os.path.join(self.quizzes_dir, quiz_filename)
        if not os.path.exists(quiz_path):
            raise ValueError(f"Quiz file not found: {quiz_filename}")
            
        # Reset server state
        self.reset_server_state()
        
        # Update current quiz and CSV filename
        self.current_quiz_file = quiz_path
        self.csv_file = self.generate_csv_path(quiz_filename)
        
        # Load new questions
        await self.load_questions_from_file(quiz_path)
        
        # Regenerate index.html with new questions
        await self.create_default_index_html()
        
        # Notify WebSocket clients about quiz switch
        await self.broadcast_to_websockets({
            'type': 'quiz_switched',
            'current_quiz': quiz_filename,
            'questions': self.questions,
            'total_questions': len(self.questions),
            'message': f'Quiz switched to: {quiz_filename}'
        })
        
        logger.info(f"Switched to quiz: {quiz_filename}, CSV: {self.csv_file}")
        
    async def create_admin_selection_page(self):
        """Create a page informing admin to select a quiz first"""
        ensure_directory_exists(self.static_dir)
        index_path = f"{self.static_dir}/index.html"
        
        # Get list of available quizzes for display
        available_quizzes = await self.list_available_quizzes()
        quiz_list_html = ""
        for quiz in available_quizzes:
            quiz_list_html += f"<li>{quiz}</li>"
        
        # Load template and replace placeholders
        template_content = self.templates.get('quiz_selection_required.html', '')
        selection_html = template_content.replace('{{QUIZ_LIST}}', quiz_list_html)

        try:
            async with aiofiles.open(index_path, 'w', encoding='utf-8') as f:
                await f.write(selection_html)
            logger.info(f"Created admin selection page: {index_path}")
        except Exception as e:
            logger.error(f"Error creating admin selection page: {e}")
        
    
    async def initialize_log_file(self):
        """Initialize new log file with unique suffix in logs directory"""
        try:
            # Generate log file path
            self.log_file = self.generate_log_path()
            # Create the new log file
            with open(self.log_file, 'w') as f:
                f.write('')
            logger.info(f"=== Server Started - New Log File Created: {self.log_file} ===")
        except Exception as e:
            print(f"Error initializing log file {self.log_file}: {e}")

    async def create_default_config_yaml(self, file_path: str = None):
        """Create default config.yaml file"""
        if file_path is None:
            file_path = self.config_file if hasattr(self, 'config_file') else 'config.yaml'
        default_questions = {
            'title': 'Тестовий Quiz',
            'show_right_answer': True,
            'questions': [
                {
                    'question': 'Скільки буде 2 + 2?',
                    'options': ['3', '4', '5', '6'],
                    'correct_answer': 1
                },
                {
                    'question': 'Яка столиця України?',
                    'options': ['Харків', 'Львів', 'Київ', 'Одеса'],
                    'correct_answer': 2
                }
            ]
        }
        
        try:
            async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
                await f.write(yaml.dump(default_questions, default_flow_style=False, allow_unicode=True))
            logger.info(f"Created default config file: {file_path}")
        except Exception as e:
            logger.error(f"Error creating default config file {file_path}: {e}")

    async def load_questions_from_file(self, quiz_file_path: str):
        """Load questions from specific quiz file for quiz execution"""
        try:
            async with aiofiles.open(quiz_file_path, 'r') as f:
                content = await f.read()
                data = yaml.safe_load(content)
                self.questions = data['questions']
                
                # Store quiz title or use default
                self.quiz_title = data.get('title', 'Система Тестування')
                
                # Store show_right_answer setting (default: True)
                self.show_right_answer = data.get('show_right_answer', True)
                
                # Add automatic IDs based on array index (for quiz execution only)
                for i, question in enumerate(self.questions):
                    question['id'] = i + 1
                        
                logger.info(f"Loaded {len(self.questions)} questions from {quiz_file_path}, show_right_answer: {self.show_right_answer}")
        except Exception as e:
            logger.error(f"Error loading questions from {quiz_file_path}: {e}")
            raise
            
    async def load_questions(self):
        """Load questions based on available quiz files"""
        try:
            # Check if quizzes directory exists
            if not os.path.exists(self.quizzes_dir):
                os.makedirs(self.quizzes_dir)
                logger.info(f"Created quizzes directory: {self.quizzes_dir}")
            
            # Get available quiz files
            available_quizzes = await self.list_available_quizzes()
            
            if not available_quizzes:
                # No quiz files found, create default
                default_path = os.path.join(self.quizzes_dir, 'default.yaml')
                await self.create_default_config_yaml(default_path)
                available_quizzes = ['default.yaml']
                await self.switch_quiz('default.yaml')
            elif len(available_quizzes) == 1:
                # Only one quiz file - use it as default
                await self.switch_quiz(available_quizzes[0])
                logger.info(f"Using single quiz file as default: {available_quizzes[0]}")
            elif 'default.yaml' in available_quizzes or 'default.yml' in available_quizzes:
                # Multiple files but default.yaml exists - use it
                default_file = 'default.yaml' if 'default.yaml' in available_quizzes else 'default.yml'
                await self.switch_quiz(default_file)
                logger.info(f"Using explicit default file: {default_file}")
            else:
                # Multiple files but no default.yaml - don't load any quiz
                logger.info(f"Multiple quiz files found but no default.yaml - admin must select quiz first")
                await self.create_admin_selection_page()
            
        except Exception as e:
            logger.error(f"Error in load_questions: {e}")
            raise
            
            
    async def create_default_index_html(self):
        """Create default index.html file with embedded questions data"""
        ensure_directory_exists(self.static_dir)
        index_path = f"{self.static_dir}/index.html"
        
        # Prepare questions data for client (without correct answers)
        questions_for_client = []
        for q in self.questions:
            client_question = {
                'id': q['id'],
                'options': q['options'],
                'is_multiple_choice': isinstance(q['correct_answer'], list)
            }
            # Include question text if present
            if 'question' in q and q['question']:
                client_question['question'] = q['question']
            # Include optional image attribute if present
            if 'image' in q and q['image']:
                client_question['image'] = q['image']
            # Include min_correct for multiple choice questions
            if isinstance(q['correct_answer'], list):
                client_question['min_correct'] = q.get('min_correct', len(q['correct_answer']))
            questions_for_client.append(client_question)
        
        # Convert questions to JSON string for embedding
        questions_json = json.dumps(questions_for_client, indent=2)
        
        # Copy template from package
        try:
            template_content = self.templates.get('index.html', '')

            # Inject questions data, title, version, and show_right_answer setting into template
            html_content = template_content.replace('{{QUESTIONS_DATA}}', questions_json)
            html_content = html_content.replace('{{QUIZ_TITLE}}', self.quiz_title)
            html_content = html_content.replace('{{SHOW_RIGHT_ANSWER}}', 'true' if self.show_right_answer else 'false')
            html_content = html_content.replace('{{WEBQUIZ_VERSION}}', get_package_version())
            
            # Write to destination
            async with aiofiles.open(index_path, 'w', encoding='utf-8') as f:
                await f.write(html_content)
                
            logger.info(f"Created index.html file with embedded questions data: {index_path}")
            return
        except Exception as e:
            logger.error(f"Error copying template index.html: {e}")
            # Continue to fallback

        # Fallback: create minimal HTML if template is not available
        try:
            fallback_html = self.templates.get('template_error.html', '<html><body><h1>Template Error</h1></body></html>')
            async with aiofiles.open(index_path, 'w', encoding='utf-8') as f:
                await f.write(fallback_html)
            logger.warning(f"Created fallback index.html file: {index_path}")
        except Exception as e:
            logger.error(f"Error creating fallback index.html: {e}")
            
    async def flush_responses_to_csv(self):
        """Flush in-memory responses to CSV file"""
        if not self.user_responses:
            return
            
        try:
            # Check if CSV file exists, if not create it with headers
            file_exists = os.path.exists(self.csv_file)
            
            # Use StringIO buffer to write CSV data
            csv_buffer = StringIO()
            csv_writer = csv.writer(csv_buffer)
            
            # Write headers if file doesn't exist
            if not file_exists:
                csv_writer.writerow(['username', 'question_text', 'selected_answer_text', 'correct_answer_text', 'is_correct', 'time_taken_seconds'])
            
            # Write all responses to buffer
            for response in self.user_responses:
                csv_writer.writerow([
                    response['username'],
                    response['question_text'],
                    response['selected_answer_text'],
                    response['correct_answer_text'],
                    response['is_correct'],
                    response['time_taken_seconds']
                ])
            
            # Write buffer content to file
            csv_content = csv_buffer.getvalue()
            csv_buffer.close()
            total_responses = len(self.user_responses)
            self.user_responses.clear()
            
            mode = 'w' if not file_exists else 'a'
            async with aiofiles.open(self.csv_file, mode) as f:
                await f.write(csv_content)
                    
            action = "Created" if not file_exists else "Updated"
            logger.info(f"{action} CSV file with {total_responses} responses: {self.csv_file}")
        except Exception as e:
            logger.error(f"Error flushing responses to CSV: {e}")
            
    async def periodic_flush(self):
        """Periodically flush responses to CSV"""
        while True:
            await asyncio.sleep(30)  # Flush every 30 seconds
            await self.flush_responses_to_csv()
    
    async def broadcast_to_websockets(self, message: dict):
        """Broadcast message to all connected WebSocket clients"""
        if not self.websocket_clients:
            return
            
        # Clean up closed connections
        active_clients = []
        for ws in self.websocket_clients:
            if not ws.closed:
                try:
                    await ws.send_str(json.dumps(message))
                    active_clients.append(ws)
                except Exception as e:
                    logger.warning(f"Failed to send message to WebSocket client: {e}")
        
        self.websocket_clients = active_clients
    
    def _validate_answer(self, selected_answer, question):
        """Validate answer for both single and multiple choice questions"""
        correct_answer = question['correct_answer']

        if isinstance(correct_answer, int):
            # Single answer question
            return selected_answer == correct_answer
        elif isinstance(correct_answer, list):
            # Multiple answer question
            if not isinstance(selected_answer, list):
                return False

            # Convert to sets for comparison
            selected_set = set(selected_answer)
            correct_set = set(correct_answer)

            # Check if any incorrect answers were selected
            if not selected_set.issubset(set(range(len(question['options'])))):
                return False  # Invalid option indices

            # Check if any incorrect answers were selected
            incorrect_selected = selected_set - correct_set
            if incorrect_selected:
                return False  # Any incorrect answer makes it wrong

            # Check minimum correct requirement
            min_correct = question.get('min_correct', len(correct_answer))
            correct_selected = selected_set & correct_set

            return len(correct_selected) >= min_correct
        else:
            return False  # Invalid correct_answer format

    def _format_answer_text(self, answer_indices, options):
        """Format answer text for CSV with | separator for multiple answers"""
        if isinstance(answer_indices, int):
            return options[answer_indices]
        elif isinstance(answer_indices, list):
            # Sort indices and join corresponding option texts with |
            sorted_indices = sorted(answer_indices)
            return '|'.join(options[idx] for idx in sorted_indices)
        else:
            return str(answer_indices)

    def update_live_stats(self, user_id: str, question_id: int, state: str, time_taken: float = None):
        """Update live stats for a user and question"""
        if user_id not in self.live_stats:
            self.live_stats[user_id] = {}
        
        # Store both state and time_taken
        self.live_stats[user_id][question_id] = {
            'state': state,
            'time_taken': time_taken
        }
            
    async def register_user(self, request):
        """Register a new user"""
        data = await request.json()
        username = data['username'].strip()
        
        if not username:
            raise ValueError('Ім\'я користувача не може бути порожнім')
            
        # Check if username already exists
        for existing_user in self.users.values():
            if existing_user['username'] == username:
                raise ValueError('Ім\'я користувача вже існує')
        
        # Generate unique user ID
        user_id = str(uuid.uuid4())
        
        self.users[user_id] = {
            'user_id': user_id,
            'username': username,
            'registered_at': datetime.now().isoformat()
        }
        
        # Start timing for first question
        self.question_start_times[user_id] = datetime.now()
        
        # Initialize live stats: set first question to "think"
        if len(self.questions) > 0:
            self.update_live_stats(user_id, 1, "think")
            
            # Broadcast new user registration
            await self.broadcast_to_websockets({
                'type': 'user_registered',
                'user_id': user_id,
                'username': username,
                'question_id': 1,
                'state': 'think',
                'time_taken': None,
                'total_questions': len(self.questions)
            })
        
        logger.info(f"Registered user: {username} with ID: {user_id}")
        return web.json_response({
            'username': username,
            'user_id': user_id,
            'message': 'User registered successfully'
        })
            
    async def submit_answer(self, request):
        """Submit test answer"""
        data = await request.json()
        user_id = data['user_id']
        question_id = data['question_id']
        selected_answer = data['selected_answer']
        
        # Find user by user_id
        if user_id not in self.users:
            return web.json_response({'error': 'Користувача не знайдено'}, status=404)
        
        username = self.users[user_id]['username']
            
        # Find the question
        question = next((q for q in self.questions if q['id'] == question_id), None)
        if not question:
            return web.json_response({'error': 'Питання не знайдено'}, status=404)
            
        # Calculate time taken server-side from when question was displayed
        time_taken = 0
        if user_id in self.question_start_times:
            time_taken = (datetime.now() - self.question_start_times[user_id]).total_seconds()
            # Clean up the start time
            del self.question_start_times[user_id]
        
        # Check if answer is correct (handle both single and multiple answers)
        is_correct = self._validate_answer(selected_answer, question)
        
        # Store response in memory
        response_data = {
            'user_id': user_id,
            'username': username,
            'question_id': question_id,
            'question_text': question.get('question', ''),  # Handle image-only questions
            'selected_answer_text': self._format_answer_text(selected_answer, question['options']),
            'correct_answer_text': self._format_answer_text(question['correct_answer'], question['options']),
            'is_correct': is_correct,
            'time_taken_seconds': time_taken,
            'timestamp': datetime.now().isoformat()
        }
        
        self.user_responses.append(response_data)
        
        # Track answer separately for stats calculation (independent of CSV flushing)
        if user_id not in self.user_answers:
            self.user_answers[user_id] = []
        
        answer_data = {
            'question': question.get('question', ''),  # Handle image-only questions
            'image': question.get('image'),
            'selected_answer': self._format_answer_text(selected_answer, question['options']),
            'correct_answer': self._format_answer_text(question['correct_answer'], question['options']),
            'is_correct': is_correct,
            'time_taken': time_taken
        }
        self.user_answers[user_id].append(answer_data)
        
        # Update user progress
        self.user_progress[user_id] = question_id
        
        # Update live stats: set current question state based on correctness
        state = "ok" if is_correct else "fail"
        self.update_live_stats(user_id, question_id, state, time_taken)
        
        # Broadcast current question result
        await self.broadcast_to_websockets({
            'type': 'state_update',
            'user_id': user_id,
            'username': username,
            'question_id': question_id,
            'state': state,
            'time_taken': time_taken,
            'total_questions': len(self.questions)
        })
        
        # Check if this was the last question and calculate final stats
        if question_id == len(self.questions):
            # Test completed - calculate and store final stats
            self.calculate_and_store_user_stats(user_id)
            logger.info(f"Test completed for user {user_id} - final stats calculated")
        
        logger.info(f"Answer submitted by {username} (ID: {user_id}) for question {question_id}: {'Correct' if is_correct else 'Incorrect'} (took {time_taken}s)")
        logger.info(f"Updated progress for user {user_id}: last answered question = {question_id}")
        
        # Prepare response data
        response_data = {
            'time_taken': time_taken,
            'message': 'Answer submitted successfully'
        }
        
        # Only include correctness feedback and correct answer if show_right_answer is enabled
        if self.show_right_answer:
            response_data['is_correct'] = is_correct
            response_data['correct_answer'] = question['correct_answer']
            response_data['is_multiple_choice'] = isinstance(question['correct_answer'], list)
        
        return web.json_response(response_data)

    async def question_start(self, request):
        """Handle notification that a user started viewing a question"""
        try:
            data = await request.json()
            user_id = data['user_id']
            question_id = data['question_id']
            username = self.users[user_id]['username']

            # Verify user exists
            if user_id not in self.users:
                return web.json_response({'error': 'Користувача не знайдено'}, status=404)

            if user_id not in self.question_start_times:
                self.question_start_times[user_id] = datetime.now()
            self.update_live_stats(user_id, question_id, "think")
            
            await self.broadcast_to_websockets({
                'type': 'state_update',
                'user_id': user_id,
                'username': username,
                'question_id': question_id,
                'state': 'think',
                'time_taken': None,
                'total_questions': len(self.questions)
            })

            return web.json_response({'status': 'success'})

        except Exception as e:
            logger.error(f"Error in question_start: {e}")
            return web.json_response({'error': 'Помилка сервера'}, status=500)

    def calculate_and_store_user_stats(self, user_id):
        """Calculate and store final stats for a completed user using user_answers (not user_responses)"""
        # Get answers from dedicated user_answers tracking (independent of CSV flushing)
        if user_id not in self.user_answers or not self.user_answers[user_id]:
            logger.warning(f"No answers found for user {user_id} during stats calculation")
            return
        
        user_answer_list = self.user_answers[user_id]
        
        # Calculate stats from user_answers
        correct_count = 0
        total_time = 0
        
        for answer in user_answer_list:
            if answer['is_correct']:
                correct_count += 1
            total_time += answer['time_taken']
        
        total_count = len(user_answer_list)
        percentage = round((correct_count / total_count) * 100) if total_count > 0 else 0
        
        # Store final stats (copy the answer data to avoid reference issues)
        self.user_stats[user_id] = {
            'test_results': [answer.copy() for answer in user_answer_list],
            'correct_count': correct_count,
            'total_count': total_count,
            'percentage': percentage,
            'total_time': total_time,
            'completed_at': datetime.now().isoformat()
        }
        
        logger.info(f"Stored final stats for user {user_id}: {correct_count}/{total_count} ({percentage}%) using user_answers")
    
    def get_user_final_results(self, user_id):
        """Get final results for a completed user from persistent user_stats"""
        if user_id in self.user_stats:
            # Return stored stats (without the completed_at timestamp for the frontend)
            stats = self.user_stats[user_id].copy()
            stats.pop('completed_at', None)  # Remove timestamp from response
            
            # If show_right_answer is disabled, remove correct answer information from test results
            if not self.show_right_answer:
                # Create a copy of test_results without correct_answer and is_correct fields
                modified_results = []
                for result in stats.get('test_results', []):
                    result_copy = result.copy()
                    result_copy.pop('correct_answer', None)  # Remove correct_answer field
                    result_copy.pop('is_correct', None)  # Remove is_correct field
                    modified_results.append(result_copy)
                stats['test_results'] = modified_results
            
            return stats
        
        # Fallback - should not happen if calculate_and_store_user_stats was called
        return {
            'test_results': [],
            'correct_count': 0,
            'total_count': 0,
            'percentage': 0,
            'total_time': 0
        }
    
    async def verify_user_id(self, request):
        """Verify if user_id exists and return user data"""
        user_id = request.match_info['user_id']
        
        # Find user by user_id
        if user_id not in self.users:
            return web.json_response({
                'valid': False,
                'message': 'User ID not found'
            })
    
        user_data = self.users[user_id]
        username = user_data['username']
        # Get last answered question ID from progress tracking
        last_answered_question_id = self.user_progress.get(user_id, 0)
        
        # Find the index of next question to answer
        next_question_index = 0
        if last_answered_question_id > 0:
            # Find the index of last answered question, then add 1
            for i, question in enumerate(self.questions):
                if question['id'] == last_answered_question_id:
                    next_question_index = i + 1
                    break
        
        # Ensure we don't go beyond available questions
        if next_question_index >= len(self.questions):
            next_question_index = len(self.questions)
        
        # Check if test is completed
        test_completed = next_question_index >= len(self.questions)
        
        response_data = {
            'valid': True,
            'user_id': user_id,
            'username': username,
            'next_question_index': next_question_index,
            'total_questions': len(self.questions),
            'last_answered_question_id': last_answered_question_id,
            'test_completed': test_completed
        }
        
        if test_completed:
            # Get final results for completed test
            final_results = self.get_user_final_results(user_id)
            response_data['final_results'] = final_results
            logger.info(f"User {user_id} verification: test completed, returning final results")
        else:
            logger.info(f"User {user_id} verification: last_answered={last_answered_question_id}, next_index={next_question_index}")
            
        return web.json_response(response_data)

    
    # Admin API endpoints
    @admin_auth_required
    async def admin_list_quizzes(self, request):
        """List available quiz files"""
        quizzes = await self.list_available_quizzes()
        return web.json_response({
            'quizzes': quizzes,
            'current_quiz': os.path.basename(self.current_quiz_file) if self.current_quiz_file else None
        })
    
    @admin_auth_required  
    async def admin_switch_quiz(self, request):
        """Switch to a different quiz"""
        try:
            data = await request.json()
            quiz_filename = data['quiz_filename']
            
            await self.switch_quiz(quiz_filename)
            
            return web.json_response({
                'success': True,
                'message': f'Switched to quiz: {quiz_filename}',
                'current_quiz': quiz_filename,
                'csv_file': os.path.basename(self.csv_file)
            })
        except Exception as e:
            logger.error(f"Error switching quiz: {e}")
            return web.json_response({'error': str(e)}, status=400)
    
    @admin_auth_required
    async def admin_auth_test(self, request):
        """Test admin authentication"""
        return web.json_response({
            'authenticated': True,
            'message': 'Admin authentication successful'
        })
    
    @admin_auth_required
    async def admin_get_quiz(self, request):
        """Get quiz content for editing"""
        try:
            filename = request.match_info['filename']
            quiz_path = os.path.join(self.quizzes_dir, filename)
            
            if not os.path.exists(quiz_path):
                return web.json_response({'error': 'Quiz file not found'}, status=404)
            
            with open(quiz_path, 'r', encoding='utf-8') as f:
                quiz_content = f.read()
            
            # Also return parsed YAML for wizard mode
            try:
                import yaml
                parsed_quiz = yaml.safe_load(quiz_content)
                return web.json_response({
                    'filename': filename,
                    'content': quiz_content,
                    'parsed': parsed_quiz
                })
            except yaml.YAMLError as e:
                return web.json_response({
                    'filename': filename,
                    'content': quiz_content,
                    'parsed': None,
                    'yaml_error': str(e)
                })
        except Exception as e:
            logger.error(f"Error getting quiz: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    @admin_auth_required
    async def admin_create_quiz(self, request):
        """Create new quiz from wizard or text input"""
        try:
            data = await request.json()
            filename = data.get('filename', '').strip()
            mode = data.get('mode', 'wizard')  # 'wizard' or 'text'
            
            if not filename:
                return web.json_response({'error': 'Filename is required'}, status=400)
            
            if not filename.endswith('.yaml'):
                filename += '.yaml'
            
            quiz_path = os.path.join(self.quizzes_dir, filename)
            
            # Check if file already exists
            if os.path.exists(quiz_path):
                return web.json_response({'error': 'Quiz file already exists'}, status=409)
            
            # Validate and create quiz content
            if mode == 'wizard':
                quiz_data = data.get('quiz_data', {})
                if not self._validate_quiz_data(quiz_data):
                    return web.json_response({'error': 'Неправильна структура даних квізу'}, status=400)
                
                import yaml
                quiz_content = yaml.dump(quiz_data, default_flow_style=False, allow_unicode=True)
            else:  # text mode
                quiz_content = data.get('content', '').strip()
                if not quiz_content:
                    return web.json_response({'error': 'Quiz content is required'}, status=400)
                
                # Validate YAML
                try:
                    import yaml
                    parsed = yaml.safe_load(quiz_content)
                    if not self._validate_quiz_data(parsed):
                        return web.json_response({'error': 'Неправильна структура даних квізу'}, status=400)
                except yaml.YAMLError as e:
                    return web.json_response({'error': f'Неправильний YAML: {str(e)}'}, status=400)
            
            # Write the quiz file
            with open(quiz_path, 'w', encoding='utf-8') as f:
                f.write(quiz_content)
            
            logger.info(f"Created new quiz: {filename}")
            return web.json_response({
                'success': True,
                'message': f'Quiz "{filename}" created successfully',
                'filename': filename
            })
        except Exception as e:
            logger.error(f"Error creating quiz: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    @admin_auth_required
    async def admin_update_quiz(self, request):
        """Update existing quiz"""
        try:
            filename = request.match_info['filename']
            data = await request.json()
            mode = data.get('mode', 'wizard')
            
            quiz_path = os.path.join(self.quizzes_dir, filename)
            
            if not os.path.exists(quiz_path):
                return web.json_response({'error': 'Quiz file not found'}, status=404)
            
            # Create backup
            backup_path = quiz_path + '.backup'
            import shutil
            shutil.copy2(quiz_path, backup_path)
            
            # Prepare new content
            if mode == 'wizard':
                quiz_data = data.get('quiz_data', {})
                if not self._validate_quiz_data(quiz_data):
                    return web.json_response({'error': 'Неправильна структура даних квізу'}, status=400)
                
                import yaml
                quiz_content = yaml.dump(quiz_data, default_flow_style=False, allow_unicode=True)
            else:  # text mode
                quiz_content = data.get('content', '').strip()
                if not quiz_content:
                    return web.json_response({'error': 'Quiz content is required'}, status=400)
                
                # Validate YAML
                try:
                    import yaml
                    parsed = yaml.safe_load(quiz_content)
                    if not self._validate_quiz_data(parsed):
                        return web.json_response({'error': 'Неправильна структура даних квізу'}, status=400)
                except yaml.YAMLError as e:
                    return web.json_response({'error': f'Неправильний YAML: {str(e)}'}, status=400)
            
            # Write updated content
            with open(quiz_path, 'w', encoding='utf-8') as f:
                f.write(quiz_content)
            
            # If this is the current quiz, reload it
            if self.current_quiz_file and os.path.basename(self.current_quiz_file) == filename:
                await self.switch_quiz(filename)
            
            logger.info(f"Updated quiz: {filename}")
            return web.json_response({
                'success': True,
                'message': f'Quiz "{filename}" updated successfully',
                'backup_created': os.path.basename(backup_path)
            })
        except Exception as e:
            logger.error(f"Error updating quiz: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    @admin_auth_required
    async def admin_delete_quiz(self, request):
        """Delete quiz file"""
        try:
            filename = request.match_info['filename']
            quiz_path = os.path.join(self.quizzes_dir, filename)
            
            if not os.path.exists(quiz_path):
                return web.json_response({'error': 'Quiz file not found'}, status=404)
            
            # Don't allow deleting the current quiz
            if self.current_quiz_file and os.path.basename(self.current_quiz_file) == filename:
                return web.json_response({'error': 'Cannot delete the currently active quiz'}, status=400)
            
            # Create backup before deletion
            backup_path = quiz_path + '.deleted_backup'
            import shutil
            shutil.copy2(quiz_path, backup_path)
            
            # Delete the file
            os.remove(quiz_path)
            
            logger.info(f"Deleted quiz: {filename} (backup: {backup_path})")
            return web.json_response({
                'success': True,
                'message': f'Quiz "{filename}" deleted successfully',
                'backup_created': os.path.basename(backup_path)
            })
        except Exception as e:
            logger.error(f"Error deleting quiz: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    @admin_auth_required
    async def admin_validate_quiz(self, request):
        """Validate quiz YAML structure"""
        try:
            data = await request.json()
            content = data.get('content', '').strip()
            
            if not content:
                return web.json_response({'valid': False, 'errors': ['Content is empty']})
            
            try:
                import yaml
                parsed = yaml.safe_load(content)
                
                # Validate structure
                errors = []
                if not self._validate_quiz_data(parsed, errors):
                    return web.json_response({'valid': False, 'errors': errors})
                
                return web.json_response({
                    'valid': True,
                    'parsed': parsed,
                    'question_count': len(parsed.get('questions', []))
                })
            except yaml.YAMLError as e:
                return web.json_response({'valid': False, 'errors': [f'YAML syntax error: {str(e)}']})
        except Exception as e:
            logger.error(f"Error validating quiz: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    def _validate_quiz_data(self, data, errors=None):
        """Validate quiz data structure"""
        if errors is None:
            errors = []
        
        if not isinstance(data, dict):
            errors.append("Дані квізу повинні бути словником")
            return False
        
        if 'questions' not in data:
            errors.append("Квіз повинен містити поле 'questions'")
            return False
        
        questions = data['questions']
        if not isinstance(questions, list):
            errors.append("'questions' повинно бути списком")
            return False
        
        if len(questions) == 0:
            errors.append("Квіз повинен містити принаймні одне питання")
            return False
        
        for i, question in enumerate(questions):
            if not isinstance(question, dict):
                errors.append(f"Question {i+1} must be a dictionary")
                continue
            
            # Validate required fields (except 'question' which is optional if image provided)
            required_fields = ['options', 'correct_answer']
            for field in required_fields:
                if field not in question:
                    errors.append(f"Question {i+1} missing required field: {field}")
            
            # Either question text OR image must be provided
            has_question = 'question' in question and question['question']
            has_image = 'image' in question and question['image']
            if not has_question and not has_image:
                errors.append(f"Question {i+1} must have either question text or image")
            
            # Validate options
            if 'options' in question:
                options = question['options']
                if not isinstance(options, list):
                    errors.append(f"Question {i+1} options must be a list")
                elif len(options) < 2:
                    errors.append(f"Question {i+1} must have at least 2 options")
                elif not all(isinstance(opt, str) for opt in options):
                    errors.append(f"Question {i+1} all options must be strings")
            
            # Validate correct_answer (can be integer for single answer or list for multiple answers)
            if 'correct_answer' in question and 'options' in question:
                correct_answer = question['correct_answer']
                options_count = len(question['options'])

                if isinstance(correct_answer, int):
                    # Single answer validation
                    if correct_answer < 0 or correct_answer >= options_count:
                        errors.append(f"Question {i+1} correct_answer index out of range")
                elif isinstance(correct_answer, list):
                    # Multiple answers validation
                    if len(correct_answer) == 0:
                        errors.append(f"Question {i+1} correct_answer array cannot be empty")
                    elif not all(isinstance(idx, int) for idx in correct_answer):
                        errors.append(f"Question {i+1} correct_answer array must contain only integers")
                    elif any(idx < 0 or idx >= options_count for idx in correct_answer):
                        errors.append(f"Question {i+1} correct_answer array contains index out of range")
                    elif len(set(correct_answer)) != len(correct_answer):
                        errors.append(f"Question {i+1} correct_answer array contains duplicate indices")
                else:
                    errors.append(f"Question {i+1} correct_answer must be an integer or array of integers")

            # Validate min_correct (only valid for multiple answers)
            if 'min_correct' in question:
                min_correct = question['min_correct']
                if 'correct_answer' not in question:
                    errors.append(f"Question {i+1} has min_correct but no correct_answer")
                elif not isinstance(question['correct_answer'], list):
                    errors.append(f"Question {i+1} min_correct is only valid for multiple answer questions")
                elif not isinstance(min_correct, int):
                    errors.append(f"Question {i+1} min_correct must be an integer")
                elif min_correct < 1:
                    errors.append(f"Question {i+1} min_correct must be at least 1")
                elif min_correct > len(question['correct_answer']):
                    errors.append(f"Question {i+1} min_correct cannot exceed number of correct answers")
        
        return len(errors) == 0
    
    @admin_auth_required
    async def admin_list_images(self, request):
        """List all images in quizzes/imgs directory"""
        try:
            imgs_dir = os.path.join(self.quizzes_dir, 'imgs')
            images = []
            
            if os.path.exists(imgs_dir) and os.path.isdir(imgs_dir):
                # Get all image files (common image extensions)
                image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'}
                
                for filename in os.listdir(imgs_dir):
                    if os.path.isfile(os.path.join(imgs_dir, filename)):
                        _, ext = os.path.splitext(filename.lower())
                        if ext in image_extensions:
                            images.append({
                                'filename': filename,
                                'path': f'/imgs/{filename}'  # Relative path for quiz usage
                            })
                
                # Sort alphabetically
                images.sort(key=lambda x: x['filename'].lower())
            
            return web.json_response({'images': images})
        except Exception as e:
            logger.error(f"Error listing images: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    @admin_auth_required
    async def admin_download_quiz(self, request):
        """Download and extract quiz from ZIP file"""
        try:
            data = await request.json()
            quiz_name = data.get('name')
            download_path = data.get('download_path')
            folder = data.get('folder')
            
            if not all([quiz_name, download_path, folder]):
                return web.json_response({'error': 'Missing required parameters'}, status=400)
            
            # Validate URL (basic HTTPS check)
            if not download_path.startswith('https://'):
                return web.json_response({'error': 'Only HTTPS URLs are allowed'}, status=400)
            
            logger.info(f"Starting download of quiz '{quiz_name}' from {download_path}")
            
            # Create temporary file for ZIP download  
            temp_zip_path = None
            try:
                with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
                    temp_zip_path = temp_zip.name
                    
                    # Download ZIP file
                    async with ClientSession() as session:
                        async with session.get(download_path) as response:
                            if response.status != 200:
                                return web.json_response(
                                    {'error': f'Failed to download: HTTP {response.status}'}, 
                                    status=400
                                )
                            
                            # Write downloaded content to temporary file
                            async for chunk in response.content.iter_chunked(8192):
                                temp_zip.write(chunk)
                
                # File is now closed, safe to open as ZIP
                with zipfile.ZipFile(temp_zip_path, 'r') as zip_file:
                    # Get all files in the specified folder
                    folder_prefix = folder if folder.endswith('/') else folder + '/'
                    files_to_extract = [f for f in zip_file.namelist() 
                                      if f.startswith(folder_prefix) and not f.endswith('/')]
                    
                    if not files_to_extract:
                        return web.json_response(
                            {'error': f'No files found in folder "{folder}" within the ZIP'}, 
                            status=400
                        )
                    
                    # Extract files to quizzes directory
                    extracted_count = 0
                    for file_path in files_to_extract:
                        # Remove folder prefix to get just the filename
                        filename = file_path[len(folder_prefix):]
                        if filename:  # Skip empty filenames
                            target_path = os.path.join(self.quizzes_dir, filename)
                            
                            # Ensure target directory exists
                            target_dir = os.path.dirname(target_path)
                            os.makedirs(target_dir, exist_ok=True)
                            
                            # Extract and write file
                            with zip_file.open(file_path) as source:
                                with open(target_path, 'wb') as target:
                                    target.write(source.read())
                            extracted_count += 1
                    
                    logger.info(f"Extracted {extracted_count} files from quiz '{quiz_name}'")
                
            finally:
                # Clean up temporary ZIP file
                if temp_zip_path:
                    try:
                        os.unlink(temp_zip_path)
                    except OSError:
                        pass
            
            # Refresh quiz list to include newly extracted files
            available_quizzes = await self.list_available_quizzes()
            
            return web.json_response({
                'success': True,
                'message': f'Successfully downloaded and extracted quiz "{quiz_name}"',
                'extracted_files': extracted_count,
                'available_quizzes': available_quizzes
            })
            
        except Exception as e:
            raise
            logger.error(f"Error downloading quiz: {e}")
            return web.json_response({'error': f'Download failed: {str(e)}'}, status=500)

    # File Management API endpoints
    async def serve_files_page(self, request):
        """Serve the files management page"""
        try:
            template_content = self.templates.get('files.html', '')

            # Check if client IP is trusted and inject auto-auth flag
            client_ip = get_client_ip(request)
            is_trusted_ip = client_ip in self.admin_config.trusted_ips if hasattr(self, 'admin_config') else False

            # Inject JavaScript variables for trusted IP auto-auth
            js_variables = f"""
                const IS_TRUSTED_IP = {str(is_trusted_ip).lower()};
            """

            # Inject the JavaScript variables before </head>
            template_content = template_content.replace('</head>', f'<script>{js_variables}</script>\n    </head>')

            return web.Response(text=template_content, content_type='text/html')
        except Exception as e:
            logger.error(f"Error serving files page: {e}")
            return web.json_response({'error': 'Failed to load files page'}, status=500)

    def _list_files_in_directory(self, directory, file_type):
        """Helper to list files in a directory with metadata"""
        files = []
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    stat = os.stat(file_path)
                    files.append({
                        'name': filename,
                        'size': stat.st_size,
                        'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                        'type': file_type
                    })
        # Sort files by modified date (newest first)
        files.sort(key=lambda x: x['modified'], reverse=True)
        return files

    @admin_auth_required
    async def files_list(self, request):
        """List all files in logs_dir and csv_dir with metadata"""
        logs_files = self._list_files_in_directory(self.logs_dir, 'log')
        csv_files = self._list_files_in_directory(self.csv_dir, 'csv')

        return web.json_response({
            'logs': logs_files,
            'csv': csv_files
        })

    def _get_file_path_and_validate(self, file_type, filename):
        """Helper to validate file type, filename, and return file path.
        Returns tuple (file_path, error_response) where error_response is None on success"""
        # Determine base directory from file type
        if file_type == 'csv':
            base_dir = self.csv_dir
        elif file_type == 'logs':
            base_dir = self.logs_dir
        else:
            return None, web.json_response({'error': 'Invalid file type'}, status=400)

        # Validate filename (prevent path traversal)
        if not self._is_safe_filename(filename):
            return None, web.json_response({'error': 'Invalid filename'}, status=400)

        file_path = os.path.join(base_dir, filename)

        # Check if file exists
        if not os.path.exists(file_path):
            return None, web.json_response({'error': 'File not found'}, status=404)

        # Check if it's actually a file (not directory)
        if not os.path.isfile(file_path):
            return None, web.json_response({'error': 'Path is not a file'}, status=400)

        return file_path, None

    @admin_auth_required
    async def files_view(self, request):
        """View file contents (text files only, with size limit)"""
        file_type = request.match_info['type']
        filename = request.match_info['filename']

        # Validate and get file path
        file_path, error = self._get_file_path_and_validate(file_type, filename)
        if error:
            return error

        # Check file size (limit to 10MB for viewing)
        MAX_VIEW_SIZE = 1024 * 1024 * 10  # 10MB
        file_size = os.path.getsize(file_path)

        if file_size > MAX_VIEW_SIZE:
            return web.json_response({
                'error': f'File too large for viewing (>10MB). Size: {file_size} bytes. Use download instead.',
                'size': file_size
            }, status=400)

        # Read file content
        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                content = await f.read()
        except UnicodeDecodeError:
            return web.json_response({'error': 'File contains non-UTF-8 content. Use download instead.'}, status=400)

        return web.Response(
            text=content,
            content_type='text/plain',
            headers={
                'Content-Disposition': f'inline; filename="{filename}"'
            }
        )

    @admin_auth_required
    async def files_download(self, request):
        """Download file directly"""
        try:
            file_type = request.match_info['type']
            filename = request.match_info['filename']

            # Validate and get file path
            file_path, error = self._get_file_path_and_validate(file_type, filename)
            if error:
                return error

            # Determine content type
            content_type = 'text/csv' if file_type == 'csv' else 'text/plain'

            # Return file response with proper headers
            return web.FileResponse(
                file_path,
                headers={
                    'Content-Disposition': f'attachment; filename="{filename}"',
                    'Content-Type': content_type
                }
            )

        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            return web.json_response({'error': 'Failed to download file'}, status=500)

    def _is_safe_filename(self, filename):
        """Check if filename is safe (no path traversal attempts)"""
        if not filename:
            return False

        # Check for path traversal attempts
        if '..' in filename or '/' in filename or '\\' in filename:
            return False

        # Check for null bytes
        if '\0' in filename:
            return False

        # Check for special filenames
        if filename in ['.', '..']:
            return False

        # Check for overly long filenames
        if len(filename) > 255:
            return False

        return True

    async def serve_index_page(self, request):
        """Serve the index.html page from static directory"""
        index_path = f"{self.static_dir}/index.html"
        return web.FileResponse(index_path, headers={'Content-Type': 'text/html'})
        
    async def serve_admin_page(self, request):
        """Serve the admin interface page"""
        try:
            template_content = self.templates.get('admin.html', '')

            # Check if client IP is trusted and inject auto-auth flag
            client_ip = get_client_ip(request)
            is_trusted_ip = client_ip in self.admin_config.trusted_ips if hasattr(self, 'admin_config') else False
            
            # Get network information (external interfaces only)
            interfaces = get_network_interfaces()  # This already excludes localhost
            port = self.config.server.port
            
            # Generate URLs for external network interfaces only
            urls = []
            for ip in interfaces:
                urls.append({
                    'label': f'Network Access ({ip})',
                    'quiz_url': f'http://{ip}:{port}/'
                })
            
            # Prepare network info for JavaScript (only what's actually used)
            network_info = {
                'urls': urls
            }
            
            # Get downloadable quizzes configuration
            downloadable_quizzes = []
            if hasattr(self.config, 'quizzes') and self.config.quizzes and self.config.quizzes.quizzes:
                for quiz in self.config.quizzes.quizzes:
                    downloadable_quizzes.append({
                        'name': quiz.name,
                        'download_path': quiz.download_path,
                        'folder': quiz.folder
                    })
            
            # Inject trusted IP status, network info, and downloadable quizzes into the template
            server_data_script = f"""
        const IS_TRUSTED_IP = {str(is_trusted_ip).lower()};
        const NETWORK_INFO = {json.dumps(network_info)};
        const DOWNLOADABLE_QUIZZES = {json.dumps(downloadable_quizzes)};"""
            
            template_content = template_content.replace(
                '<script>',
                f'<script>{server_data_script}\n'
            )
            
            return web.Response(text=template_content, content_type='text/html')
        except Exception as e:
            logger.error(f"Error serving admin page: {e}")
            return web.Response(text='<h1>Admin page not found</h1>', content_type='text/html', status=404)
    
    async def serve_live_stats_page(self, request):
        """Serve the live stats page"""
        try:
            template_content = self.templates.get('live_stats.html', '')

            return web.Response(text=template_content, content_type='text/html')
        except Exception as e:
            logger.error(f"Error serving live stats page: {e}")
            return web.Response(text='<h1>Live stats page not found</h1>', content_type='text/html', status=404)
    
    async def websocket_live_stats(self, request):
        """WebSocket endpoint for live stats updates"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        
        # Add to connected clients
        self.websocket_clients.append(ws)
        logger.info(f"New WebSocket client connected. Total clients: {len(self.websocket_clients)}")
        
        # Send initial state
        try:
            initial_data = {
                'type': 'initial_state',
                'live_stats': self.live_stats,
                'users': {user_id: user_data['username'] for user_id, user_data in self.users.items()},
                'questions': self.questions,
                'total_questions': len(self.questions),
                'current_quiz': os.path.basename(self.current_quiz_file) if self.current_quiz_file else None
            }
            await ws.send_str(json.dumps(initial_data))
        except Exception as e:
            logger.error(f"Error sending initial state to WebSocket client: {e}")
        
        # Listen for messages (mainly for connection keep-alive)
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                try:
                    data = json.loads(msg.data)
                    if data.get('type') == 'ping':
                        await ws.send_str(json.dumps({'type': 'pong'}))
                except Exception as e:
                    logger.warning(f"Error processing WebSocket message: {e}")
            elif msg.type == WSMsgType.ERROR:
                logger.error(f'WebSocket error: {ws.exception()}')
                break
        
        # Remove from connected clients when connection closes
        if ws in self.websocket_clients:
            self.websocket_clients.remove(ws)
        logger.info(f"WebSocket client disconnected. Total clients: {len(self.websocket_clients)}")
        
        return ws

async def create_app(config: WebQuizConfig):
    """Create and configure the application"""
    
    server = TestingServer(config)
    
    # Initialize log file first (this will set server.log_file)
    await server.initialize_log_file()
    
    # Configure logging with the actual log file path
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(server.log_file),
            logging.StreamHandler()  # Also log to console
        ],
        force=True  # Override any existing configuration
    )
    
    # Load questions and create HTML with embedded data (CSV will be initialized in switch_quiz)
    await server.load_questions()
    
    # Start periodic flush task
    asyncio.create_task(server.periodic_flush())
    
    # Create app with middleware
    app = web.Application(middlewares=[error_middleware])
    
    # Routes
    app.router.add_post('/api/register', server.register_user)
    app.router.add_post('/api/submit-answer', server.submit_answer)
    app.router.add_post('/api/question-start', server.question_start)
    app.router.add_get('/api/verify-user/{user_id}', server.verify_user_id)
    
    # Admin routes
    app.router.add_get('/admin/', server.serve_admin_page)
    app.router.add_post('/api/admin/auth', server.admin_auth_test)
    app.router.add_get('/api/admin/list-quizzes', server.admin_list_quizzes)
    app.router.add_post('/api/admin/switch-quiz', server.admin_switch_quiz)
    app.router.add_get('/api/admin/quiz/{filename}', server.admin_get_quiz)
    app.router.add_post('/api/admin/create-quiz', server.admin_create_quiz)
    app.router.add_put('/api/admin/quiz/{filename}', server.admin_update_quiz)
    app.router.add_delete('/api/admin/quiz/{filename}', server.admin_delete_quiz)
    app.router.add_post('/api/admin/validate-quiz', server.admin_validate_quiz)
    app.router.add_get('/api/admin/list-images', server.admin_list_images)
    app.router.add_post('/api/admin/download-quiz', server.admin_download_quiz)

    # File management routes (admin access)
    app.router.add_get('/files/', server.serve_files_page)
    app.router.add_get('/api/files/list', server.files_list)
    app.router.add_get('/api/files/{type}/view/{filename}', server.files_view)
    app.router.add_get('/api/files/{type}/download/{filename}', server.files_download)

    # Live stats routes (public access)
    app.router.add_get('/live-stats/', server.serve_live_stats_page)
    app.router.add_get('/ws/live-stats', server.websocket_live_stats)
    
    # Serve index.html at root path
    app.router.add_get('/', server.serve_index_page)
    
    # Ensure imgs directory exists before serving static files
    ensure_directory_exists(os.path.join(config.paths.quizzes_dir, 'imgs'))
    app.router.add_static(
        '/imgs/', 
        path=os.path.join(config.paths.quizzes_dir, 'imgs'),
        show_index=True,
        name='imgs',
    )
    # Serve static files from configured static directory
    app.router.add_static('/', path=config.paths.static_dir, name='static')
    
    return app

# Server is now started via CLI (aiotests.cli:main)