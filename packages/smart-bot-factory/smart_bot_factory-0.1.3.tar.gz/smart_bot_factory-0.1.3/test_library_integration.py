"""
Тест интеграции новых модулей в библиотеку
"""
import asyncio
import logging
from smart_bot_factory import (
    check_timeouts,
    test_admin_system,
    check_setup,
    setup_bot_environment,
    Config,
    SupabaseClient,
    AdminManager,
    ConversationManager,
    AnalyticsManager
)

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

async def test_integration():
    """Тестирует интеграцию новых модулей"""
    bot_name = "new-valera"  # Используем существующего бота
    
    logger.info("🔍 Тест интеграции новых модулей")
    logger.info(f"Тестируем на боте: {bot_name}\n")
    
    # 1. Проверяем setup_bot_environment
    logger.info("1️⃣ Тест setup_bot_environment:")
    config_dir = setup_bot_environment(bot_name)
    if not config_dir:
        logger.error("❌ setup_bot_environment не работает")
        return False
    logger.info("✅ setup_bot_environment работает\n")
    
    # 2. Проверяем check_setup
    logger.info("2️⃣ Тест check_setup:")
    setup_ok = await check_setup(bot_name)
    if not setup_ok:
        logger.error("❌ check_setup не работает")
        return False
    logger.info("✅ check_setup работает\n")
    
    # 3. Проверяем check_timeouts
    logger.info("3️⃣ Тест check_timeouts:")
    timeouts_ok = await check_timeouts(bot_name)
    if not timeouts_ok:
        logger.error("❌ check_timeouts не работает")
        return False
    logger.info("✅ check_timeouts работает\n")
    
    # 4. Проверяем test_admin_system
    logger.info("4️⃣ Тест test_admin_system:")
    admin_ok = await test_admin_system(bot_name)
    if not admin_ok:
        logger.error("❌ test_admin_system не работает")
        return False
    logger.info("✅ test_admin_system работает\n")
    
    # 5. Проверяем взаимодействие компонентов
    logger.info("5️⃣ Тест взаимодействия компонентов:")
    try:
        # Инициализируем конфигурацию
        config = Config()
        logger.info("✅ Config инициализирован")
        
        # Инициализируем Supabase
        supabase = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await supabase.initialize()
        logger.info("✅ SupabaseClient инициализирован")
        
        # Инициализируем AdminManager
        admin_manager = AdminManager(config, supabase)
        logger.info("✅ AdminManager инициализирован")
        
        # Инициализируем ConversationManager
        conversation_manager = ConversationManager(supabase, admin_manager)
        logger.info("✅ ConversationManager инициализирован")
        
        # Инициализируем AnalyticsManager
        analytics_manager = AnalyticsManager(supabase)
        logger.info("✅ AnalyticsManager инициализирован")
        
        # Проверяем получение данных
        conversations = await conversation_manager.get_active_conversations()
        logger.info(f"✅ Получено {len(conversations)} активных диалогов")
        
        stats = await analytics_manager.get_funnel_stats(1)
        logger.info("✅ Получена статистика воронки")
        
    except Exception as e:
        logger.error(f"❌ Ошибка взаимодействия компонентов: {e}")
        return False
    
    logger.info("\n🎉 Все тесты пройдены успешно!")
    return True

if __name__ == "__main__":
    try:
        success = asyncio.run(test_integration())
        if not success:
            logger.error("\n❌ Тесты не пройдены")
            exit(1)
    except KeyboardInterrupt:
        logger.info("\n⏹️ Прервано пользователем")
    except Exception as e:
        logger.error(f"\n💥 Критическая ошибка: {e}")
        logger.exception("Стек ошибки:")
        exit(1)
