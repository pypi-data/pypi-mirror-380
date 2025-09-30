"""
Сервисы для работы с внешними API
"""

from .telegram_integration import TelegramIntegration
from .message_sender import send_message_by_ai, send_message_by_human

__all__ = [
    'TelegramIntegration',
    'send_message_by_ai',
    'send_message_by_human'
]
