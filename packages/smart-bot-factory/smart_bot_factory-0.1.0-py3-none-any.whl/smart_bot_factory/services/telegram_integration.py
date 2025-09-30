"""
Интеграция с Telegram API через существующие функции
"""

import logging
from typing import Optional, Dict, Any, List
from aiogram import Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import FSInputFile

logger = logging.getLogger(__name__)

class TelegramIntegration:
    """Интеграция с Telegram API через существующие функции из bot_utils.py"""
    
    def __init__(self, bot_token: str):
        """
        Инициализация интеграции
        
        Args:
            bot_token: Токен Telegram бота
        """
        self.bot = Bot(token=bot_token)
        self._bot_token = bot_token
    
    async def send_message(
        self, 
        user_id: int, 
        text: str, 
        parse_mode: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        files_list: List[str] = None,
        directories_list: List[str] = None
    ) -> Dict[str, Any]:
        """
        Отправляет сообщение пользователю через существующую функцию send_message
        
        Args:
            user_id: ID пользователя в Telegram
            text: Текст сообщения
            parse_mode: Режим парсинга (Markdown, HTML, None)
            reply_markup: Клавиатура для сообщения
            files_list: Список файлов для отправки
            directories_list: Список каталогов для отправки
            
        Returns:
            Результат отправки
        """
        try:
            # Создаем фиктивное сообщение для использования существующей функции
            from aiogram.types import User, Chat
            from aiogram.types import Message as MessageType
            
            # Создаем фиктивного пользователя
            fake_user = User(
                id=user_id,
                is_bot=False,
                first_name="User"
            )
            
            # Создаем фиктивный чат
            fake_chat = Chat(
                id=user_id,
                type="private"
            )
            
            # Создаем фиктивное сообщение
            fake_message = MessageType(
                message_id=1,
                from_user=fake_user,
                chat=fake_chat,
                date=0,
                content_type="text",
                text=""
            )
            
            # Импортируем существующую функцию
            from ..integrations import send_message
            
            # Используем существующую функцию
            await send_message(
                fake_message, 
                text, 
                files_list=files_list or [], 
                directories_list=directories_list or [],
                **({"parse_mode": parse_mode} if parse_mode else {}),
                **({"reply_markup": reply_markup} if reply_markup else {})
            )
            
            return {
                "status": "success",
                "user_id": user_id,
                "text": text,
                "message": "Сообщение отправлено через существующую функцию"
            }
            
        except Exception as e:
            logger.error(f"Ошибка отправки сообщения пользователю {user_id}: {e}")
            return {
                "status": "error",
                "error": str(e),
                "user_id": user_id
            }
    
    async def send_document(
        self,
        user_id: int,
        document_path: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Отправляет документ пользователю
        
        Args:
            user_id: ID пользователя в Telegram
            document_path: Путь к документу
            caption: Подпись к документу
            parse_mode: Режим парсинга
            
        Returns:
            Результат отправки
        """
        try:
            document = FSInputFile(document_path)
            message = await self.bot.send_document(
                chat_id=user_id,
                document=document,
                caption=caption,
                parse_mode=parse_mode
            )
            
            return {
                "status": "success",
                "message_id": message.message_id,
                "user_id": user_id,
                "document_path": document_path
            }
            
        except Exception as e:
            logger.error(f"Ошибка отправки документа пользователю {user_id}: {e}")
            return {
                "status": "error",
                "error": str(e),
                "user_id": user_id
            }
    
    async def send_photo(
        self,
        user_id: int,
        photo_path: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Отправляет фото пользователю
        
        Args:
            user_id: ID пользователя в Telegram
            photo_path: Путь к фото
            caption: Подпись к фото
            parse_mode: Режим парсинга
            
        Returns:
            Результат отправки
        """
        try:
            photo = FSInputFile(photo_path)
            message = await self.bot.send_photo(
                chat_id=user_id,
                photo=photo,
                caption=caption,
                parse_mode=parse_mode
            )
            
            return {
                "status": "success",
                "message_id": message.message_id,
                "user_id": user_id,
                "photo_path": photo_path
            }
            
        except Exception as e:
            logger.error(f"Ошибка отправки фото пользователю {user_id}: {e}")
            return {
                "status": "error",
                "error": str(e),
                "user_id": user_id
            }
    
    async def send_chat_action(self, user_id: int, action: str) -> Dict[str, Any]:
        """
        Отправляет действие чата (typing, uploading_photo, etc.)
        
        Args:
            user_id: ID пользователя в Telegram
            action: Действие (typing, uploading_photo, uploading_document, etc.)
            
        Returns:
            Результат отправки действия
        """
        try:
            await self.bot.send_chat_action(chat_id=user_id, action=action)
            
            return {
                "status": "success",
                "user_id": user_id,
                "action": action
            }
            
        except Exception as e:
            logger.error(f"Ошибка отправки действия пользователю {user_id}: {e}")
            return {
                "status": "error",
                "error": str(e),
                "user_id": user_id
            }
    
    def create_keyboard(self, buttons: List[List[Dict[str, str]]]) -> InlineKeyboardMarkup:
        """
        Создает клавиатуру из кнопок
        
        Args:
            buttons: Список рядов кнопок [[{"text": "Кнопка", "callback_data": "data"}], ...]
            
        Returns:
            InlineKeyboardMarkup
        """
        keyboard_buttons = []
        
        for row in buttons:
            row_buttons = []
            for button in row:
                row_buttons.append(InlineKeyboardButton(
                    text=button["text"],
                    callback_data=button.get("callback_data", "")
                ))
            keyboard_buttons.append(row_buttons)
        
        return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    
    async def close(self):
        """Закрывает сессию бота"""
        if self.bot:
            await self.bot.session.close()
