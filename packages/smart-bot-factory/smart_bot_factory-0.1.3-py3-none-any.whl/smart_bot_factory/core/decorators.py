"""
Декораторы для обработчиков событий и временных задач
"""

import asyncio
import logging
from typing import Callable, Any, Dict, Optional
from datetime import datetime, timedelta
from functools import wraps

logger = logging.getLogger(__name__)

# Глобальный реестр обработчиков событий
_event_handlers: Dict[str, Callable] = {}
_scheduled_tasks: Dict[str, Dict[str, Any]] = {}

def event_handler(event_type: str, description: str = ""):
    """
    Декоратор для регистрации обработчика события
    
    Args:
        event_type: Тип события (например, 'appointment_booking', 'phone_collection')
        description: Описание что делает обработчик (для добавления в промпт)
    
    Example:
        @event_handler("appointment_booking", "Записывает пользователя на прием")
        async def book_appointment(user_id: int, appointment_data: dict):
            # Логика записи на прием
            return {"status": "success", "appointment_id": "123"}
    """
    def decorator(func: Callable) -> Callable:
        _event_handlers[event_type] = {
            'handler': func,
            'description': description,
            'name': func.__name__
        }
        
        logger.info(f"📝 Зарегистрирован обработчик события '{event_type}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"🔧 Выполняем обработчик события '{event_type}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Обработчик '{event_type}' выполнен успешно")
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в обработчике '{event_type}': {e}")
                raise
        
        return wrapper
    return decorator

def schedule_task(task_name: str, description: str = ""):
    """
    Декоратор для регистрации задачи, которую можно запланировать на время
    
    Args:
        task_name: Название задачи (например, 'send_reminder', 'follow_up')
        description: Описание задачи (для добавления в промпт)
    
    Example:
        @schedule_task("send_reminder", "Отправляет напоминание пользователю")
        async def send_reminder(user_id: int, message: str):
            # Логика отправки напоминания
            return {"status": "sent"}
    """
    def decorator(func: Callable) -> Callable:
        _scheduled_tasks[task_name] = {
            'handler': func,
            'description': description,
            'name': func.__name__
        }
        
        logger.info(f"⏰ Зарегистрирована задача '{task_name}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"⏰ Выполняем запланированную задачу '{task_name}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Задача '{task_name}' выполнена успешно")
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в задаче '{task_name}': {e}")
                raise
        
        return wrapper
    return decorator

def get_event_handlers() -> Dict[str, Dict[str, Any]]:
    """Возвращает все зарегистрированные обработчики событий"""
    return _event_handlers.copy()

def get_scheduled_tasks() -> Dict[str, Dict[str, Any]]:
    """Возвращает все зарегистрированные задачи"""
    return _scheduled_tasks.copy()

def get_handlers_for_prompt() -> str:
    """
    Возвращает описание всех обработчиков для добавления в промпт
    """
    if not _event_handlers and not _scheduled_tasks:
        return ""
    
    prompt_parts = []
    
    if _event_handlers:
        prompt_parts.append("ДОСТУПНЫЕ ОБРАБОТЧИКИ СОБЫТИЙ:")
        for event_type, handler_info in _event_handlers.items():
            prompt_parts.append(f"- {event_type}: {handler_info['description']}")
    
    if _scheduled_tasks:
        prompt_parts.append("\nДОСТУПНЫЕ ЗАДАЧИ ДЛЯ ПЛАНИРОВАНИЯ:")
        for task_name, task_info in _scheduled_tasks.items():
            prompt_parts.append(f"- {task_name}: {task_info['description']}")
    
    return "\n".join(prompt_parts)

async def execute_event_handler(event_type: str, *args, **kwargs) -> Any:
    """Выполняет обработчик события по типу"""
    if event_type not in _event_handlers:
        raise ValueError(f"Обработчик события '{event_type}' не найден")
    
    handler_info = _event_handlers[event_type]
    return await handler_info['handler'](*args, **kwargs)

async def execute_scheduled_task(task_name: str, *args, **kwargs) -> Any:
    """Выполняет запланированную задачу по имени"""
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    task_info = _scheduled_tasks[task_name]
    return await task_info['handler'](*args, **kwargs)

async def schedule_task_for_later(task_name: str, delay_seconds: int, *args, **kwargs):
    """
    Планирует выполнение задачи через указанное время
    
    Args:
        task_name: Название задачи
        delay_seconds: Задержка в секундах
        *args, **kwargs: Аргументы для задачи
    """
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    logger.info(f"⏰ Планируем задачу '{task_name}' через {delay_seconds} секунд")
    
    async def delayed_task():
        await asyncio.sleep(delay_seconds)
        await execute_scheduled_task(task_name, *args, **kwargs)
    
    # Запускаем задачу в фоне
    asyncio.create_task(delayed_task())
    
    return {
        "status": "scheduled",
        "task_name": task_name,
        "delay_seconds": delay_seconds,
        "scheduled_at": datetime.now().isoformat()
    }

async def execute_scheduled_task_from_event(user_id: int, task_name: str, event_info: str):
    """
    Выполняет запланированную задачу на основе события от ИИ
    
    Args:
        user_id: ID пользователя
        task_name: Название задачи
        event_info: Информация от ИИ (содержит время и сообщение)
    """
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    # Парсим event_info для извлечения времени и сообщения
    # Формат: "через 2 часа: напомнить о приеме"
    try:
        if ":" in event_info:
            time_part, message = event_info.split(":", 1)
            time_part = time_part.strip()
            message = message.strip()
        else:
            time_part = event_info
            message = "Напоминание"
        
        # Парсим время
        delay_seconds = _parse_time_to_seconds(time_part)
        
        # Планируем задачу
        result = await schedule_task_for_later(task_name, delay_seconds, user_id, message)
        
        return result
        
    except Exception as e:
        logger.error(f"Ошибка парсинга времени из event_info '{event_info}': {e}")
        # Fallback - планируем через 1 час
        return await schedule_task_for_later(task_name, 3600, user_id, event_info)

def _parse_time_to_seconds(time_str: str) -> int:
    """
    Парсит строку времени в секунды
    Поддерживает форматы:
    - "через 2 часа"
    - "через 30 минут" 
    - "через 1 день"
    - "через 2 часа 30 минут"
    """
    import re
    
    time_str = time_str.lower().strip()
    
    # Ищем часы
    hours_match = re.search(r'(\d+)\s*час', time_str)
    hours = int(hours_match.group(1)) if hours_match else 0
    
    # Ищем минуты
    minutes_match = re.search(r'(\d+)\s*минут', time_str)
    minutes = int(minutes_match.group(1)) if minutes_match else 0
    
    # Ищем дни
    days_match = re.search(r'(\d+)\s*дн', time_str)
    days = int(days_match.group(1)) if days_match else 0
    
    # Конвертируем в секунды
    total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60)
    
    # Минимум 1 минута
    return max(total_seconds, 60)
