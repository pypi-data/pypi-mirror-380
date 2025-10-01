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

def event_handler(event_type: str, description: str = "", notify: bool = False):
    """
    Декоратор для регистрации обработчика события
    
    Args:
        event_type: Тип события (например, 'appointment_booking', 'phone_collection')
        description: Описание что делает обработчик (для добавления в промпт)
        notify: Уведомлять ли админов о выполнении события (по умолчанию False)
    
    Example:
        @event_handler("appointment_booking", "Записывает пользователя на прием", notify=True)
        async def book_appointment(user_id: int, appointment_data: dict):
            # Логика записи на прием
            return {"status": "success", "appointment_id": "123"}
    """
    def decorator(func: Callable) -> Callable:
        _event_handlers[event_type] = {
            'handler': func,
            'description': description,
            'name': func.__name__,
            'notify': notify
        }
        
        logger.info(f"📝 Зарегистрирован обработчик события '{event_type}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"🔧 Выполняем обработчик события '{event_type}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Обработчик '{event_type}' выполнен успешно")
                
                # Автоматически добавляем флаг notify к результату
                if isinstance(result, dict):
                    result['notify'] = notify
                else:
                    # Если результат не словарь, создаем словарь
                    result = {
                        'status': 'success',
                        'result': result,
                        'notify': notify
                    }
                
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в обработчике '{event_type}': {e}")
                raise
        
        return wrapper
    return decorator

def schedule_task(task_name: str, description: str = "", notify: bool = False):
    """
    Декоратор для регистрации задачи, которую можно запланировать на время
    
    Args:
        task_name: Название задачи (например, 'send_reminder', 'follow_up')
        description: Описание задачи (для добавления в промпт)
        notify: Уведомлять ли админов о выполнении задачи (по умолчанию False)
    
    Example:
        @schedule_task("send_reminder", "Отправляет напоминание пользователю", notify=False)
        async def send_reminder(user_id: int, user_data: dict):
            # user_data содержит: {"delay_seconds": 3600, "scheduled_at": "..."}
            delay_seconds = user_data.get("delay_seconds", 0)
            # Логика отправки напоминания (выполняется на фоне)
            return {"status": "sent", "delay_seconds": delay_seconds}
    """
    def decorator(func: Callable) -> Callable:
        _scheduled_tasks[task_name] = {
            'handler': func,
            'description': description,
            'name': func.__name__,
            'notify': notify
        }
        
        logger.info(f"⏰ Зарегистрирована задача '{task_name}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"⏰ Выполняем запланированную задачу '{task_name}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Задача '{task_name}' выполнена успешно")
                
                # Автоматически добавляем флаг notify к результату
                if isinstance(result, dict):
                    result['notify'] = notify
                else:
                    # Если результат не словарь, создаем словарь
                    result = {
                        'status': 'success',
                        'result': result,
                        'notify': notify
                    }
                
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

async def execute_scheduled_task(task_name: str, user_id: int, user_data: dict) -> Any:
    """Выполняет запланированную задачу по имени"""
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    task_info = _scheduled_tasks[task_name]
    return await task_info['handler'](user_id, user_data)

async def schedule_task_for_later(task_name: str, delay_seconds: int, user_id: int, user_data: dict):
    """
    Планирует выполнение задачи через указанное время
    
    Args:
        task_name: Название задачи
        delay_seconds: Задержка в секундах
        user_id: ID пользователя
        user_data: Данные для задачи
    """
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    logger.info(f"⏰ Планируем задачу '{task_name}' через {delay_seconds} секунд")
    
    async def delayed_task():
        await asyncio.sleep(delay_seconds)
        await execute_scheduled_task(task_name, user_id, user_data)
    
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
        event_info: Информация от ИИ (содержит время в секундах и сообщение)
    """
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    try:
        # ИИ присылает время в секундах, парсим его
        delay_seconds = int(event_info)
        
        # Создаем user_data с временем в секундах
        user_data = {
            "delay_seconds": delay_seconds,
            "scheduled_at": datetime.now().isoformat()
        }
        
        # Планируем задачу на фоне
        result = await schedule_task_for_later(task_name, delay_seconds, user_id, user_data)
        
        return result
        
    except ValueError as e:
        logger.error(f"Ошибка парсинга времени из event_info '{event_info}': {e}")
        # Fallback - планируем через 1 час
        user_data = {
            "delay_seconds": 3600,
            "scheduled_at": datetime.now().isoformat()
        }
        return await schedule_task_for_later(task_name, 3600, user_id, user_data)

