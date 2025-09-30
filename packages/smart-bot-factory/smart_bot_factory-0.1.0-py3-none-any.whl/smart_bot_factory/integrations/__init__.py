"""
Интеграции с существующими файлами проекта
"""

# Импортируем существующие классы из корня проекта
import sys
from pathlib import Path

# Добавляем корень проекта в путь для импорта существующих файлов
project_root = Path(__file__).parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from openai_client import OpenAIClient
    from supabase_client import SupabaseClient
    from config import Config
    from conversation_manager import ConversationManager
    from admin_manager import AdminManager
    from prompt_loader import PromptLoader
    from bot_utils import send_message, parse_ai_response, process_events
    from handlers import router, setup_handlers
    from admin_logic import setup_admin_handlers
    from bot_utils import setup_utils_handlers
except ImportError as e:
    # Если файлы не найдены, создаем заглушки
    print(f"⚠️ Предупреждение: не удалось импортировать существующие файлы: {e}")
    
    class OpenAIClient:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("OpenAIClient не найден. Убедитесь, что openai_client.py существует в корне проекта")
    
    class SupabaseClient:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("SupabaseClient не найден. Убедитесь, что supabase_client.py существует в корне проекта")
    
    class Config:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Config не найден. Убедитесь, что config.py существует в корне проекта")
    
    class ConversationManager:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("ConversationManager не найден. Убедитесь, что conversation_manager.py существует в корне проекта")
    
    class AdminManager:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("AdminManager не найден. Убедитесь, что admin_manager.py существует в корне проекта")
    
    class PromptLoader:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("PromptLoader не найден. Убедитесь, что prompt_loader.py существует в корне проекта")
    
    # Заглушки для функций
    def send_message(*args, **kwargs):
        raise NotImplementedError("send_message не найден. Убедитесь, что bot_utils.py существует в корне проекта")
    
    def parse_ai_response(*args, **kwargs):
        raise NotImplementedError("parse_ai_response не найден. Убедитесь, что bot_utils.py существует в корне проекта")
    
    def process_events(*args, **kwargs):
        raise NotImplementedError("process_events не найден. Убедитесь, что bot_utils.py существует в корне проекта")
    
    # Заглушки для роутера
    router = None
    setup_handlers = None
    setup_admin_handlers = None
    setup_utils_handlers = None

__all__ = [
    'OpenAIClient',
    'SupabaseClient', 
    'Config',
    'ConversationManager',
    'AdminManager',
    'PromptLoader',
    'send_message',
    'parse_ai_response', 
    'process_events',
    'router',
    'setup_handlers',
    'setup_admin_handlers',
    'setup_utils_handlers'
]
