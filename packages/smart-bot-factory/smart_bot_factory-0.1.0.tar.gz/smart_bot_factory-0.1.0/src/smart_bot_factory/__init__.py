"""
Smart Bot Factory - библиотека для создания умных чат-ботов
"""

from .core.bot_builder import BotBuilder
from .events.decorators import event_handler, schedule_task
from .integrations import (
    OpenAIClient,
    SupabaseClient,
    Config,
    ConversationManager,
    AdminManager,
    PromptLoader
)
from .services import send_message_by_ai, send_message_by_human

__version__ = "0.1.0"
__all__ = [
    'BotBuilder',
    'event_handler',
    'schedule_task',
    'OpenAIClient',
    'SupabaseClient',
    'Config',
    'ConversationManager',
    'AdminManager',
    'PromptLoader',
    'send_message_by_ai',
    'send_message_by_human'
]
