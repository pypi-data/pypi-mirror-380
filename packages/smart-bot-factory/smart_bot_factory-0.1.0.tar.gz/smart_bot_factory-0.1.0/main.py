# Исправленный main.py с корректной передачей bot_id в SupabaseClient

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config
from supabase_client import SupabaseClient
from openai_client import OpenAIClient
from prompt_loader import PromptLoader
from admin_manager import AdminManager
from conversation_manager import ConversationManager
from analytics_manager import AnalyticsManager

from handlers import setup_handlers
from admin_logic import setup_admin_handlers
from bot_utils import cleanup_expired_conversations, setup_utils_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Глобальные переменные для доступа из других модулей
config = None
bot = None
dp = None
supabase_client = None
openai_client = None
prompt_loader = None
admin_manager = None
conversation_manager = None
analytics_manager = None

def init_components():
    """Инициализация всех компонентов системы"""
    global config, bot, dp, supabase_client, openai_client, prompt_loader
    global admin_manager, conversation_manager, analytics_manager
    
    # Инициализация конфигурации
    config = Config()
    
    # Инициализация бота и диспетчера
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # 🆕 Инициализация Supabase клиента С bot_id для мультиботовой архитектуры
    supabase_client = SupabaseClient(
        url=config.SUPABASE_URL, 
        key=config.SUPABASE_KEY,
        bot_id=config.BOT_ID  # 🆕 Передаем bot_id для изоляции данных между ботами
    )
    
    # Инициализация OpenAI клиента
    openai_client = OpenAIClient(
        api_key=config.OPENAI_API_KEY,
        model=config.OPENAI_MODEL,
        max_tokens=config.OPENAI_MAX_TOKENS,
        temperature=config.OPENAI_TEMPERATURE
    )
    
    # Инициализация загрузчика промптов
    prompt_loader = PromptLoader(
        prompts_dir=config.PROMT_FILES_DIR, 
        prompt_files=config.PROMPT_FILES
    )
    
    # Инициализация новых менеджеров админской системы
    admin_manager = AdminManager(config, supabase_client)
    conversation_manager = ConversationManager(supabase_client, admin_manager)
    analytics_manager = AnalyticsManager(supabase_client)
    
    logger.info(f"✅ Все компоненты инициализированы для bot_id: {config.BOT_ID}")

async def main():
    """Главная функция"""
    try:
        # Инициализируем компоненты
        init_components()
        
        # Инициализируем базу данных
        await supabase_client.initialize()
        
        # Синхронизируем админов из конфигурации
        await admin_manager.sync_admins_from_config()
        
        # Проверяем доступность промптов
        prompts_status = await prompt_loader.validate_prompts()
        logger.info(f"Статус промптов: {prompts_status}")
        
        # Настраиваем обработчики запросов
        setup_utils_handlers(dp)    # Утилитарные команды (/status, /help)
        setup_admin_handlers(dp)    # Админские команды (/админ, /стат, /чат)
        setup_handlers(dp)          # Основные пользовательские обработчики
        
        # Запускаем фоновую задачу очистки просроченных диалогов
        asyncio.create_task(cleanup_expired_conversations())
        
        logger.info(f"🚀 Бот {config.BOT_ID.upper()} успешно запущен с мультиботовой архитектурой!")
        logger.info(f"   📊 Изоляция данных: bot_id = {config.BOT_ID}")
        logger.info(f"   👑 Админов настроено: {len(config.ADMIN_TELEGRAM_IDS)}")
        logger.info(f"   📝 Загружено промптов: {len(config.PROMPT_FILES)}")
        
        # Запуск polling (бесконечная обработка сообщений)
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"💥 Критическая ошибка при запуске бота {config.BOT_ID if config else 'UNKNOWN'}: {e}")
        import traceback
        logger.error(f"Стек ошибки: {traceback.format_exc()}")
        raise
    finally:
        # Очистка ресурсов при завершении
        if bot:
            await bot.session.close()
        logger.info(f"⏹️ Бот {config.BOT_ID if config else 'UNKNOWN'} корректно остановлен")

if __name__ == "__main__":
    asyncio.run(main())