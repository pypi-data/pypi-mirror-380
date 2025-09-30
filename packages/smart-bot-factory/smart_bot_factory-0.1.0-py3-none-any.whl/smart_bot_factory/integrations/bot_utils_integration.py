"""
Интеграция с bot_utils.py для обработки событий
"""

import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

async def enhanced_process_events(session_id: str, events: List[Dict[str, Any]], user_id: int):
    """
    Улучшенная версия process_events из bot_utils.py
    с поддержкой декораторов обработчиков событий
    """
    from ..events.decorators import (
        execute_event_handler, 
        get_event_handlers, 
        get_scheduled_tasks,
        execute_scheduled_task_from_event
    )
    
    logger.info(f"🔔 Обрабатываем {len(events)} событий для пользователя {user_id}")
    
    for event in events:
        try:
            event_type = event.get('тип', '')
            event_info = event.get('инфо', '')
            
            if not event_type:
                continue
            
            logger.info(f"📝 Обрабатываем событие: {event_type}")
            
            # Проверяем, есть ли зарегистрированный обработчик событий
            event_handlers = get_event_handlers()
            scheduled_tasks = get_scheduled_tasks()
            
            if event_type in event_handlers:
                # Используем зарегистрированный обработчик событий
                logger.info(f"🔧 Используем зарегистрированный обработчик для '{event_type}'")
                
                try:
                    # Парсим event_info если это строка
                    if isinstance(event_info, str):
                        event_data = _parse_event_info(event_info, user_id)
                    else:
                        event_data = event_info
                    
                    # Вызываем обработчик
                    result = await execute_event_handler(event_type, user_id, event_data)
                    logger.info(f"✅ Обработчик '{event_type}' выполнен: {result}")
                    
                except Exception as e:
                    logger.error(f"❌ Ошибка в обработчике '{event_type}': {e}")
                    # Fallback к стандартной обработке
                    await _fallback_event_processing(session_id, event_type, event_info, user_id)
                    
            elif event_type in scheduled_tasks:
                # Это запланированная задача - парсим время из event_info
                logger.info(f"⏰ Планируем задачу '{event_type}' на основе event_info: {event_info}")
                
                try:
                    result = await execute_scheduled_task_from_event(user_id, event_type, event_info)
                    logger.info(f"✅ Задача '{event_type}' запланирована: {result}")
                    
                except Exception as e:
                    logger.error(f"❌ Ошибка в планировании задачи '{event_type}': {e}")
                    # Fallback к стандартной обработке
                    await _fallback_event_processing(session_id, event_type, event_info, user_id)
            else:
                # Используем стандартную обработку из bot_utils.py
                logger.info(f"📋 Используем стандартную обработку для '{event_type}'")
                await _fallback_event_processing(session_id, event_type, event_info, user_id)
            
        except Exception as e:
            logger.error(f"❌ Ошибка при обработке события {event}: {e}")

def _parse_event_info(event_info: str, user_id: int) -> Dict[str, Any]:
    """
    Парсит строку event_info и извлекает структурированные данные
    """
    # Простой парсинг для типичных случаев
    # Например: "Иван Петров, +7-999-123-45-67, интересуется имплантацией"
    
    data = {
        "user_id": user_id,
        "raw_info": event_info
    }
    
    # Пытаемся извлечь телефон
    import re
    phone_match = re.search(r'\+?[7-8]?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}', event_info)
    if phone_match:
        data["phone"] = phone_match.group(0)
    
    # Пытаемся извлечь имя (первое слово)
    words = event_info.split(',')
    if words:
        data["name"] = words[0].strip()
    
    # Пытаемся извлечь услугу/интерес
    if len(words) > 2:
        data["interest"] = words[2].strip()
    
    return data

async def _fallback_event_processing(session_id: str, event_type: str, event_info: str, user_id: int):
    """
    Стандартная обработка событий (из оригинального bot_utils.py)
    """
    # Импортируем оригинальную функцию
    import sys
    from pathlib import Path
    
    # Добавляем корень проекта в путь
    project_root = Path(__file__).parent.parent.parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    try:
        from supabase_client import SupabaseClient
        from main import supabase_client
        
        # Сохраняем в БД
        await supabase_client.add_session_event(session_id, event_type, event_info)
        
        # Уведомляем админов
        await _notify_admins_about_event(user_id, {
            'тип': event_type,
            'инфо': event_info
        })
        
    except ImportError:
        logger.warning("Не удалось импортировать оригинальные модули для fallback обработки")

async def _notify_admins_about_event(user_id: int, event: Dict[str, Any]):
    """
    Уведомление админов о событии (из оригинального bot_utils.py)
    """
    try:
        import sys
        from pathlib import Path
        
        # Добавляем корень проекта в путь
        project_root = Path(__file__).parent.parent.parent.parent
        if str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))
        
        from main import supabase_client, admin_manager, bot
        from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
        from datetime import datetime
        
        event_type = event.get('тип', '')
        event_info = event.get('инфо', '')
        
        if not event_type:
            return
        
        # Получаем информацию о пользователе
        try:
            user_response = supabase_client.client.table('sales_users').select(
                'first_name', 'last_name', 'username'
            ).eq('telegram_id', user_id).execute()
            
            user_info = user_response.data[0] if user_response.data else {}
            
            # Формируем имя пользователя
            name_parts = []
            if user_info.get('first_name'):
                name_parts.append(user_info['first_name'])
            if user_info.get('last_name'):
                name_parts.append(user_info['last_name'])
            
            user_name = " ".join(name_parts) if name_parts else "Без имени"
            
            # Формируем отображение пользователя
            if user_info.get('username'):
                user_display = f"{user_name} (@{user_info['username']})"
            else:
                user_display = user_name
                
        except Exception as e:
            logger.error(f"Ошибка получения информации о пользователе {user_id}: {e}")
            user_display = "Пользователь"
        
        # Маппинг эмодзи
        emoji_map = {
            'телефон': '📱',
            'консультация': '💬',
            'покупка': '💰',
            'отказ': '❌',
            'appointment_booking': '📅',
            'phone_collection': '📱'
        }
        
        emoji = emoji_map.get(event_type, '🔔')
        
        # Формируем уведомление
        notification = f"""
{emoji} {event_type.upper()}!
👤 {user_display}
🆔 ID: {user_id}
📝 {event_info}
🕐 {datetime.now().strftime('%H:%M')}
"""
        
        # Создаем клавиатуру
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="💬 Чат", callback_data=f"admin_chat_{user_id}"),
                InlineKeyboardButton(text="📋 История", callback_data=f"admin_history_{user_id}")
            ]
        ])
        
        # Отправляем всем активным админам
        active_admins = await admin_manager.get_active_admins()
        for admin_id in active_admins:
            try:
                await bot.send_message(admin_id, notification.strip(), reply_markup=keyboard)
            except Exception as e:
                logger.error(f"Ошибка отправки уведомления админу {admin_id}: {e}")
                
    except Exception as e:
        logger.error(f"Ошибка отправки уведомления админам: {e}")
