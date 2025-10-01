"""
Smart Bot Factory - библиотека для создания умных чат-ботов
"""

from .creation.bot_builder import BotBuilder
from .core.decorators import event_handler, schedule_task
from .core.message_sender import send_message_by_ai, send_message_by_human
from .config import Config
from .integrations.openai_client import OpenAIClient
from .integrations.supabase_client import SupabaseClient
from .core.conversation_manager import ConversationManager
from .admin.admin_manager import AdminManager
from .utils.prompt_loader import PromptLoader
from .handlers.handlers import setup_handlers
from .admin.admin_logic import setup_admin_handlers
from .core.bot_utils import setup_utils_handlers, parse_ai_response, process_events
from .utils.debug_routing import setup_debug_handlers
from .core.states import UserStates, AdminStates
from .creation.bot_testing import main as bot_testing_main
from .analytics.analytics_manager import AnalyticsManager
from .admin.timeout_checker import check_timeouts, setup_bot_environment
from .setup_checker import check_setup
from .admin.admin_tester import test_admin_system

__all__ = [
    'BotBuilder',
    'event_handler',
    'schedule_task',
    'send_message_by_ai',
    'send_message_by_human',
    'Config',
    'OpenAIClient',
    'SupabaseClient',
    'ConversationManager',
    'AdminManager',
    'PromptLoader',
    'setup_handlers',
    'setup_admin_handlers',
    'setup_utils_handlers',
    'parse_ai_response',
    'process_events',
    'setup_debug_handlers',
    'UserStates',
    'AdminStates',
    'bot_testing_main',
    'AnalyticsManager',
    'check_timeouts',
    'setup_bot_environment',
    'check_setup',
    'test_admin_system',
]
