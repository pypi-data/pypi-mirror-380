"""
Функции для отправки сообщений через ИИ и от человека
"""

import logging
import time
from datetime import datetime
from typing import Dict, Any, Optional
import pytz

logger = logging.getLogger(__name__)

async def send_message_by_ai(
    user_id: int, 
    message_text: str, 
    session_id: str = None
) -> Dict[str, Any]:
    """
    Отправляет сообщение пользователю через ИИ (копирует логику process_user_message)
    
    Args:
        user_id: ID пользователя в Telegram
        message_text: Текст сообщения для обработки ИИ
        session_id: ID сессии чата (если не указан, будет использована активная сессия)
        
    Returns:
        Результат отправки
    """
    try:
        # Импортируем необходимые компоненты
        from .bot_utils import parse_ai_response, process_events
        from .config import Config
        from .openai_client import OpenAIClient
        from .supabase_client import SupabaseClient
        from .prompt_loader import PromptLoader
        from aiogram import Bot

        # Получаем компоненты из глобального контекста
        from .handlers import get_global_var
        bot = get_global_var('bot')
        supabase_client = get_global_var('supabase_client')
        openai_client = get_global_var('openai_client')
        config = get_global_var('config')
        prompt_loader = get_global_var('prompt_loader')
        
        # Если session_id не указан, получаем активную сессию пользователя
        if not session_id:
            session_info = await supabase_client.get_active_session(user_id)
            if not session_info:
                return {
                    "status": "error",
                    "error": "Активная сессия не найдена",
                    "user_id": user_id
                }
            session_id = session_info['id']
        
        # Загружаем системный промпт
        try:
            system_prompt = await prompt_loader.load_system_prompt()
            logger.info(f"✅ Системный промпт загружен ({len(system_prompt)} символов)")
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки системного промпта: {e}")
            return {
                "status": "error",
                "error": "Не удалось загрузить системный промпт",
                "user_id": user_id
            }
        
        # Сохраняем сообщение пользователя в БД
        await supabase_client.add_message(
            session_id=session_id,
            role='user',
            content=message_text,
            message_type='text'
        )
        logger.info(f"✅ Сообщение пользователя сохранено в БД")
        
        # Получаем историю сообщений
        chat_history = await supabase_client.get_chat_history(session_id, limit=config.MAX_CONTEXT_MESSAGES)
        logger.info(f"📚 Загружена история: {len(chat_history)} сообщений")
        
        # Добавляем текущее время
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz)
        time_info = current_time.strftime('%H:%M, %d.%m.%Y, %A')
        
        # Модифицируем системный промпт, добавляя время
        system_prompt_with_time = f"""
{system_prompt}

ТЕКУЩЕЕ ВРЕМЯ: {time_info} (московское время)
"""
        
        # Формируем контекст для OpenAI
        messages = [{"role": "system", "content": system_prompt_with_time}]
        
        for msg in chat_history[-config.MAX_CONTEXT_MESSAGES:]:
            messages.append({
                "role": msg['role'],
                "content": msg['content']
            })
        
        # Добавляем финальные инструкции
        final_instructions = await prompt_loader.load_final_instructions()
        if final_instructions:
            messages.append({"role": "system", "content": final_instructions})
            logger.info(f"🎯 Добавлены финальные инструкции")
        
        logger.info(f"📝 Контекст сформирован: {len(messages)} сообщений")
        
        # Отправляем действие "печатает"
        await bot.send_chat_action(user_id, "typing")
        
        # Получаем ответ от ИИ
        start_time = time.time()
        ai_response = await openai_client.get_completion(messages)
        processing_time = int((time.time() - start_time) * 1000)
        
        logger.info(f"🤖 OpenAI ответил за {processing_time}мс")
        
        # Обрабатываем ответ
        tokens_used = 0
        ai_metadata = {}
        response_text = ""
        
        if not ai_response or not ai_response.strip():
            logger.warning(f"❌ OpenAI вернул пустой ответ!")
            fallback_message = "Извините, произошла техническая ошибка. Попробуйте переформулировать вопрос."
            ai_response = fallback_message
            response_text = fallback_message
        else:
            tokens_used = openai_client.estimate_tokens(ai_response)
            response_text, ai_metadata = parse_ai_response(ai_response)
            
            if not ai_metadata:
                response_text = ai_response
                ai_metadata = {}
            elif not response_text.strip():
                response_text = ai_response
        
        # Обновляем этап сессии и качество лида
        if ai_metadata:
            stage = ai_metadata.get('этап')
            quality = ai_metadata.get('качество')
            
            if stage or quality is not None:
                await supabase_client.update_session_stage(session_id, stage, quality)
                logger.info(f"✅ Этап и качество обновлены в БД")
            
            # Обрабатываем события
            events = ai_metadata.get('события', [])
            if events:
                logger.info(f"🔔 Обрабатываем {len(events)} событий")
                await process_events(session_id, events, user_id)
        
        # Сохраняем ответ ассистента
        await supabase_client.add_message(
            session_id=session_id,
            role='assistant',
            content=response_text,
            message_type='text',
            tokens_used=tokens_used,
            processing_time_ms=processing_time,
            ai_metadata=ai_metadata
        )
        
        # Определяем финальный ответ
        if config.DEBUG_MODE:
            final_response = ai_response
        else:
            final_response = response_text
        
        # Отправляем ответ пользователю напрямую через бота
        await bot.send_message(
            chat_id=user_id,
            text=final_response
        )
        
        return {
            "status": "success",
            "user_id": user_id,
            "response_text": response_text,
            "tokens_used": tokens_used,
            "processing_time_ms": processing_time,
            "events_processed": len(events) if events else 0
        }
        
    except Exception as e:
        logger.error(f"❌ Ошибка в send_message_by_ai: {e}")
        return {
            "status": "error",
            "error": str(e),
            "user_id": user_id
        }

async def send_message_by_human(
    user_id: int, 
    message_text: str,
    session_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Отправляет сообщение пользователю от имени человека (готовый текст)
    
    Args:
        user_id: ID пользователя в Telegram
        message_text: Готовый текст сообщения
        session_id: ID сессии (опционально, для сохранения в БД)
        
    Returns:
        Результат отправки
    """
    try:
        # Импортируем необходимые компоненты
        from .handlers import get_global_var
        bot = get_global_var('bot')
        supabase_client = get_global_var('supabase_client')
        
        # Отправляем сообщение пользователю
        message = await bot.send_message(
            chat_id=user_id,
            text=message_text
        )
        
        # Если указана сессия, сохраняем сообщение в БД
        if session_id:
            await supabase_client.add_message(
                session_id=session_id,
                role='assistant',
                content=message_text,
                message_type='text',
                metadata={'sent_by_human': True}
            )
            logger.info(f"💾 Сообщение от человека сохранено в БД")
        
        return {
            "status": "success",
            "user_id": user_id,
            "message_id": message.message_id,
            "message_text": message_text,
            "saved_to_db": bool(session_id)
        }
        
    except Exception as e:
        logger.error(f"❌ Ошибка в send_message_by_human: {e}")
        return {
            "status": "error",
            "error": str(e),
            "user_id": user_id
        }
