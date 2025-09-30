# Полностью исправленный скрипт для проверки корректности таймаутов диалогов админов

import asyncio
import logging
from datetime import datetime, timezone
from pathlib import Path
import sys
import os
from dotenv import load_dotenv

def setup_bot_environment(bot_name: str = "growthmed-october-24"):
    """Настраивает окружение для указанного бота с автоопределением BOT_ID"""
    root_dir = Path(__file__).parent
    config_dir = root_dir / 'configs' / bot_name
    
    print(f"🔍 Ищем конфигурацию бота в: {config_dir}")
    
    if not config_dir.exists():
        print(f"❌ Папка конфигурации не найдена: {config_dir}")
        print(f"   Доступные боты:")
        configs_dir = root_dir / 'configs'
        if configs_dir.exists():
            for bot_dir in configs_dir.iterdir():
                if bot_dir.is_dir():
                    print(f"     - {bot_dir.name}")
        return None
    
    # Проверяем наличие промптов
    prompts_dir = config_dir / 'prompts'
    if not prompts_dir.exists():
        print(f"❌ Папка с промптами не найдена: {prompts_dir}")
        return None
    
    print(f"✅ Найдена папка промптов: {prompts_dir}")
    
    # 🆕 КРИТИЧЕСКИ ВАЖНО: Устанавливаем BOT_ID ИЗ ИМЕНИ БОТА
    os.environ['BOT_ID'] = bot_name
    print(f"🤖 Автоматически установлен BOT_ID: {bot_name}")
    
    # Загружаем .env из конфигурации бота
    env_file = config_dir / '.env'
    if env_file.exists():
        print(f"🔧 Загружаем .env из: {env_file}")
        load_dotenv(env_file)
    else:
        print(f"❌ Файл .env не найден: {env_file}")
        return None
    
    # 🔧 ИСПРАВЛЕНИЕ: Сохраняем текущую директорию и меняем её
    original_cwd = os.getcwd()
    os.chdir(str(config_dir))
    print(f"📁 Изменена рабочая директория: {os.getcwd()}")
    
    # Добавляем корневую директорию в sys.path для импорта модулей
    if str(root_dir) not in sys.path:
        sys.path.insert(0, str(root_dir))
    
    # Проверяем что промпты доступны относительно новой директории
    local_prompts = Path('prompts')
    if local_prompts.exists():
        print(f"✅ Промпты доступны из рабочей директории: {local_prompts.absolute()}")
    else:
        print(f"❌ Промпты не найдены в рабочей директории: {local_prompts.absolute()}")
        os.chdir(original_cwd)  # Восстанавливаем директорию
        return None
    
    return config_dir

async def check_timeouts():
    """Проверяет корректность таймаутов"""
    
    print("🔍 Проверка таймаутов диалогов админов\n")
    
    # Определяем какого бота проверять
    bot_name = "growthmed-october-24"  # по умолчанию
    if len(sys.argv) > 1:
        bot_name = sys.argv[1]
    
    print(f"🚀 Проверка для бота: {bot_name}")
    print(f"🤖 Bot ID будет автоопределен как: {bot_name}\n")
    
    # Настраиваем окружение для бота (автоматически устанавливает BOT_ID)
    config_dir = setup_bot_environment(bot_name)
    if not config_dir:
        print("❌ Не удалось настроить окружение бота")
        return
    
    print(f"📁 Текущая рабочая директория: {os.getcwd()}")
    print(f"📂 Содержимое рабочей директории:")
    for item in Path('.').iterdir():
        if item.is_dir():
            print(f"   📁 {item.name}/")
        else:
            print(f"   📄 {item.name}")
    print()
    
    # 🔧 ИСПРАВЛЕНИЕ: Импортируем модули ПОСЛЕ настройки окружения
    try:
        print("📦 Импортируем модули...")
        
        # Импортируем по одному для лучшей диагностики
        print("   - Импорт config...")
        from config import Config
        
        print("   - Импорт supabase_client...")
        from supabase_client import SupabaseClient
        
        print("   - Импорт conversation_manager...")
        from conversation_manager import ConversationManager
        
        print("   - Импорт admin_manager...")
        from admin_manager import AdminManager
        
        print("✅ Все модули импортированы успешно\n")
        
    except Exception as e:
        print(f"❌ Ошибка импорта модулей: {e}")
        import traceback
        print(f"Стек ошибки: {traceback.format_exc()}")
        return
    
    # Инициализация
    try:
        print("⚙️ Инициализация конфигурации...")
        config = Config()
        print(f"✅ Конфигурация загружена")
        
        print("🔗 Подключение к Supabase...")
        supabase_client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await supabase_client.initialize()
        print(f"✅ Supabase подключен")
        
        print("👑 Инициализация менеджеров...")
        admin_manager = AdminManager(config, supabase_client)
        conversation_manager = ConversationManager(supabase_client, admin_manager)
        print(f"✅ Менеджеры инициализированы\n")
        
    except Exception as e:
        print(f"❌ Ошибка инициализации: {e}")
        import traceback
        print(f"Стек ошибки: {traceback.format_exc()}")
        return
    
    print(f"⚙️ Конфигурация:")
    print(f"   BOT_ID: {config.BOT_ID}")
    print(f"   ADMIN_SESSION_TIMEOUT_MINUTES: {config.ADMIN_SESSION_TIMEOUT_MINUTES}")
    print(f"   PROMT_FILES_DIR: {config.PROMT_FILES_DIR}")
    print(f"   Найдено промпт-файлов: {len(config.PROMPT_FILES)}")
    print(f"   Админов: {len(config.ADMIN_TELEGRAM_IDS)}")
    print(f"   Сейчас UTC: {datetime.now(timezone.utc)}")
    print()
    
    # Получаем активные диалоги
    try:
        print("📊 Получение активных диалогов...")
        conversations = await conversation_manager.get_active_conversations()
        print(f"✅ Получено {len(conversations)} диалогов")
    except Exception as e:
        print(f"❌ Ошибка получения диалогов: {e}")
        return
    
    if not conversations:
        print("💬 Нет активных диалогов")
        print("💡 Создайте диалог командой /чат USER_ID для тестирования")
        
        # Показываем пример создания тестового диалога
        print(f"\n🧪 Пример создания тестового диалога:")
        print(f"1. Запустите бота: python {bot_name}.py")
        print(f"2. Как админ выполните: /чат 123456789")
        print(f"3. Затем проверьте: /чаты")
        return
    
    print(f"📊 Найдено {len(conversations)} активных диалогов:")
    print()
    
    problems_found = 0
    
    for i, conv in enumerate(conversations, 1):
        print(f"{i}. Диалог ID: {conv['id']}")
        print(f"   👤 Пользователь: {conv['user_id']}")
        print(f"   👑 Админ: {conv['admin_id']}")
        
        # Анализируем времена
        started_at_str = conv['started_at']
        auto_end_str = conv['auto_end_at']
        
        print(f"   🕐 started_at (сырое): {started_at_str}")
        print(f"   ⏰ auto_end_at (сырое): {auto_end_str}")
        
        try:
            # Парсим время начала с правильной обработкой timezone
            if started_at_str.endswith('Z'):
                start_time = datetime.fromisoformat(started_at_str.replace('Z', '+00:00'))
            elif '+' in started_at_str or started_at_str.count(':') >= 3:
                start_time = datetime.fromisoformat(started_at_str)
            else:
                naive_time = datetime.fromisoformat(started_at_str)
                start_time = naive_time.replace(tzinfo=timezone.utc)
            
            # Парсим время автозавершения с правильной обработкой timezone
            if auto_end_str.endswith('Z'):
                auto_end = datetime.fromisoformat(auto_end_str.replace('Z', '+00:00'))
            elif '+' in auto_end_str or auto_end_str.count(':') >= 3:
                auto_end = datetime.fromisoformat(auto_end_str)
            else:
                naive_time = datetime.fromisoformat(auto_end_str)
                auto_end = naive_time.replace(tzinfo=timezone.utc)
            
            print(f"   📅 start_time (parsed): {start_time}")
            print(f"   ⏰ auto_end (parsed): {auto_end}")
            
            # Планируемая длительность
            planned_duration = auto_end - start_time
            planned_minutes = int(planned_duration.total_seconds() / 60)
            print(f"   📏 Планируемая длительность: {planned_minutes} минут")
            
            # Текущее время в UTC
            now_utc = datetime.now(timezone.utc)
            
            # Приводим все к UTC для корректных расчетов
            if start_time.tzinfo != timezone.utc:
                start_time_utc = start_time.astimezone(timezone.utc)
            else:
                start_time_utc = start_time
                
            if auto_end.tzinfo != timezone.utc:
                auto_end_utc = auto_end.astimezone(timezone.utc)
            else:
                auto_end_utc = auto_end
            
            # Прошло времени
            elapsed = now_utc - start_time_utc
            elapsed_minutes = max(0, int(elapsed.total_seconds() / 60))
            print(f"   ⏱️ Прошло времени: {elapsed_minutes} минут")
            
            # Оставшееся время
            remaining = auto_end_utc - now_utc
            remaining_minutes = max(0, int(remaining.total_seconds() / 60))
            print(f"   ⏰ Осталось времени: {remaining_minutes} минут")
            
            # Проверяем корректность конфигурации
            expected_timeout = config.ADMIN_SESSION_TIMEOUT_MINUTES
            if abs(planned_minutes - expected_timeout) <= 2:  # допускаем погрешность 2 минуты
                print(f"   ✅ Таймаут корректный (ожидался {expected_timeout} мин)")
            else:
                print(f"   ❌ ОШИБКА: ожидался {expected_timeout} мин, получили {planned_minutes} мин")
                problems_found += 1
            
            # Проверяем математику
            total_check = elapsed_minutes + remaining_minutes
            print(f"   🔢 Проверка: {elapsed_minutes} + {remaining_minutes} = {total_check} мин")
            
            if abs(total_check - planned_minutes) > 2:
                print(f"   ⚠️ ПРОБЛЕМА: сумма не сходится! Возможна проблема с timezone")
                problems_found += 1
            else:
                print(f"   ✅ Математика сходится")
                
        except Exception as e:
            print(f"   ❌ Ошибка парсинга: {e}")
            problems_found += 1
            import traceback
            print(f"   Стек ошибки: {traceback.format_exc()}")
        
        print()
    
    # Тестируем функцию форматирования
    print("🧪 Тестирование format_active_conversations:")
    try:
        formatted_text = conversation_manager.format_active_conversations(conversations)
        print(formatted_text)
    except Exception as e:
        print(f"❌ Ошибка форматирования: {e}")
        problems_found += 1
    
    # Итоговый результат
    print(f"\n{'='*50}")
    print(f"📊 ИТОГОВЫЙ РЕЗУЛЬТАТ:")
    if problems_found == 0:
        print("✅ Все таймауты корректны!")
    else:
        print(f"❌ Найдено {problems_found} проблем")
        print("💡 Запустите fix_existing_timeouts.py для исправления")
    print(f"{'='*50}")

if __name__ == "__main__":
    # Убираем лишние логи для чистого вывода
    logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')
    
    print("🔍 Утилита проверки таймаутов диалогов")
    print("Использование:")
    print("  python check_timeouts.py [bot_name]")
    print("  python check_timeouts.py growthmed-october-24")
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        exit(0)
    
    try:
        asyncio.run(check_timeouts())
    except KeyboardInterrupt:
        print("\n⏹️ Прервано пользователем")
    except Exception as e:
        print(f"\n💥 Критическая ошибка: {e}")
        import traceback
        print(f"Стек ошибки: {traceback.format_exc()}")