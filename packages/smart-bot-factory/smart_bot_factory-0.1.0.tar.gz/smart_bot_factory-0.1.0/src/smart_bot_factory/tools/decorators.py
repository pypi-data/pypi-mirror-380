"""
Декораторы для инструментов AI (Function Calling)
"""

import json
import logging
from typing import Callable, Any, Dict, List, Optional
from functools import wraps

logger = logging.getLogger(__name__)

# Глобальный реестр инструментов AI
_ai_tools: Dict[str, Dict[str, Any]] = {}

def ai_tool(name: str, description: str, parameters_schema: Dict[str, Any]):
    """
    Декоратор для регистрации инструмента AI (Function Calling)
    
    Args:
        name: Название инструмента
        description: Описание инструмента для AI
        parameters_schema: JSON Schema параметров
    
    Example:
        @ai_tool(
            name="book_appointment",
            description="Записать пользователя на прием к врачу",
            parameters_schema={
                "type": "object",
                "properties": {
                    "user_id": {"type": "integer", "description": "ID пользователя"},
                    "service": {"type": "string", "description": "Название услуги"},
                    "datetime": {"type": "string", "description": "Дата и время"}
                },
                "required": ["user_id", "service", "datetime"]
            }
        )
        async def book_appointment(user_id: int, service: str, datetime: str):
            # Логика записи на прием
            return {"status": "success", "appointment_id": "123"}
    """
    def decorator(func: Callable) -> Callable:
        _ai_tools[name] = {
            'handler': func,
            'description': description,
            'parameters_schema': parameters_schema,
            'name': func.__name__
        }
        
        logger.info(f"🔧 Зарегистрирован AI инструмент '{name}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"🤖 AI вызывает инструмент '{name}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ AI инструмент '{name}' выполнен успешно")
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в AI инструменте '{name}': {e}")
                raise
        
        return wrapper
    return decorator

def get_ai_tools() -> Dict[str, Dict[str, Any]]:
    """Возвращает все зарегистрированные AI инструменты"""
    return _ai_tools.copy()

def get_openai_tools_schema() -> List[Dict[str, Any]]:
    """
    Возвращает схему инструментов в формате OpenAI Function Calling
    """
    tools = []
    for tool_name, tool_info in _ai_tools.items():
        tools.append({
            "type": "function",
            "function": {
                "name": tool_name,
                "description": tool_info['description'],
                "parameters": tool_info['parameters_schema']
            }
        })
    
    return tools

def get_tools_for_prompt() -> str:
    """
    Возвращает описание всех AI инструментов для добавления в промпт
    """
    if not _ai_tools:
        return ""
    
    prompt_parts = ["ДОСТУПНЫЕ ИНСТРУМЕНТЫ AI:"]
    
    for tool_name, tool_info in _ai_tools.items():
        prompt_parts.append(f"- {tool_name}: {tool_info['description']}")
        
        # Добавляем информацию о параметрах
        required_params = tool_info['parameters_schema'].get('required', [])
        if required_params:
            prompt_parts.append(f"  Обязательные параметры: {', '.join(required_params)}")
    
    return "\n".join(prompt_parts)

async def execute_ai_tool(tool_name: str, arguments: Dict[str, Any]) -> Any:
    """Выполняет AI инструмент по имени с аргументами"""
    if tool_name not in _ai_tools:
        raise ValueError(f"AI инструмент '{tool_name}' не найден")
    
    tool_info = _ai_tools[tool_name]
    handler = tool_info['handler']
    
    # Валидируем аргументы по схеме
    _validate_tool_arguments(tool_name, arguments, tool_info['parameters_schema'])
    
    return await handler(**arguments)

def _validate_tool_arguments(tool_name: str, arguments: Dict[str, Any], schema: Dict[str, Any]):
    """Валидирует аргументы инструмента по JSON Schema"""
    required_params = schema.get('required', [])
    
    # Проверяем обязательные параметры
    for param in required_params:
        if param not in arguments:
            raise ValueError(f"Отсутствует обязательный параметр '{param}' для инструмента '{tool_name}'")
    
    # Проверяем типы параметров
    properties = schema.get('properties', {})
    for param_name, param_value in arguments.items():
        if param_name in properties:
            param_schema = properties[param_name]
            expected_type = param_schema.get('type')
            
            if expected_type == 'integer' and not isinstance(param_value, int):
                raise ValueError(f"Параметр '{param_name}' должен быть integer для инструмента '{tool_name}'")
            elif expected_type == 'string' and not isinstance(param_value, str):
                raise ValueError(f"Параметр '{param_name}' должен быть string для инструмента '{tool_name}'")
            elif expected_type == 'boolean' and not isinstance(param_value, bool):
                raise ValueError(f"Параметр '{param_name}' должен быть boolean для инструмента '{tool_name}'")
