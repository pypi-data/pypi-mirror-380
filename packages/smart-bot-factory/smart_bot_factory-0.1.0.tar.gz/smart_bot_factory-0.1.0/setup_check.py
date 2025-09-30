#!/usr/bin/env python3
"""
Скрипт для проверки настройки Telegram Sales Bot v2.0 (с админской системой)
Запуск: 
  python setup_check.py                           # для growthmed-october-24 (по умолчанию)
  python setup_check.py growthmed-october-24      # явно указать бота
  python setup_check.py другой-бот               # для других ботов
"""

import asyncio
import logging
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_bot_environment(bot_name: str = "growthmed-october-24"):
    """Настраивает окружение для указанного бота с автоопределением BOT_ID"""
    root_dir = Path(__file__).parent
    config_dir = root_dir / 'configs' / bot_name
    
    if not config_dir.exists():
        print(f"❌ Папка конфигурации не найдена: {config_dir}")
        print(f"   Доступные боты:")
        configs_dir = root_dir / 'configs'
        if configs_dir.exists():
            for bot_dir in configs_dir.iterdir():
                if bot_dir.is_dir():
                    print(f"     - {bot_dir.name}")
        return None
    
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
    
    # Меняем рабочую директорию
    os.chdir(str(config_dir))
    print(f"📁 Рабочая директория: {config_dir}")
    
    # Добавляем корневую директорию в sys.path для импорта модулей
    if str(root_dir) not in sys.path:
        sys.path.insert(0, str(root_dir))
    
    return config_dir


async def check_config():
    """Проверяем конфигурацию с новыми админскими настройками"""
    try:
        from config import Config
        config = Config()
        
        print("✅ Конфигурация загружена успешно")
        print(f"📋 Сводка конфигурации:")
        
        summary = config.get_summary()
        for key, value in summary.items():
            print(f"   • {key}: {value}")
        
        # Проверяем админские настройки
        print(f"\n👑 Админские настройки:")
        print(f"   • Админов настроено: {len(config.ADMIN_TELEGRAM_IDS)}")
        if config.ADMIN_TELEGRAM_IDS:
            print(f"   • ID админов: {config.ADMIN_TELEGRAM_IDS}")
        print(f"   • Таймаут сессий: {config.ADMIN_SESSION_TIMEOUT_MINUTES} мин")
        print(f"   • Режим отладки: {'Включен' if config.DEBUG_MODE else 'Выключен'}")
        
        return config
    except Exception as e:
        print(f"❌ Ошибка конфигурации: {e}")
        return None

async def check_supabase(config):
    """Проверяем подключение к Supabase и новые таблицы"""
    try:
        from supabase_client import SupabaseClient
        
        client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await client.initialize()
        
        # Пробуем выполнить простой запрос к основной таблице
        response = client.client.table('sales_users').select('id').limit(1).execute()
        print("✅ Supabase подключение успешно")
        
        # Проверяем новые таблицы админской системы
        admin_tables = [
            'sales_admins',
            'admin_user_conversations', 
            'session_events'
        ]
        
        print("🔍 Проверка админских таблиц:")
        for table in admin_tables:
            try:
                response = client.client.table(table).select('*').limit(1).execute()
                print(f"   ✅ {table}")
            except Exception as e:
                print(f"   ❌ {table}: {e}")
        
        # Проверяем новые колонки
        print("🔍 Проверка новых колонок:")
        try:
            response = client.client.table('sales_chat_sessions').select(
                'current_stage', 'lead_quality_score'
            ).limit(1).execute()
            print("   ✅ sales_chat_sessions: current_stage, lead_quality_score")
        except Exception as e:
            print(f"   ❌ sales_chat_sessions новые колонки: {e}")
        
        try:
            response = client.client.table('sales_messages').select('ai_metadata').limit(1).execute()
            print("   ✅ sales_messages: ai_metadata")
        except Exception as e:
            print(f"   ❌ sales_messages.ai_metadata: {e}")
        
        return True
    except Exception as e:
        print(f"❌ Ошибка Supabase: {e}")
        return False

async def check_openai(config):
    """Проверяем OpenAI API"""
    try:
        from openai_client import OpenAIClient
        
        client = OpenAIClient(
            config.OPENAI_API_KEY,
            config.OPENAI_MODEL,
            config.OPENAI_MAX_TOKENS,
            config.OPENAI_TEMPERATURE
        )
        
        health = await client.check_api_health()
        
        if health:
            print("✅ OpenAI API доступен")
            
            # Получаем список доступных моделей
            models = await client.get_available_models()
            if config.OPENAI_MODEL in models:
                print(f"✅ Модель {config.OPENAI_MODEL} доступна")
            else:
                print(f"⚠️ Модель {config.OPENAI_MODEL} не найдена в доступных")
                print(f"   Доступные модели: {models[:5]}...")
        
        return health
    except Exception as e:
        print(f"❌ Ошибка OpenAI: {e}")
        return False

async def check_prompts(config):
    """Проверяем промпты с новыми JSON инструкциями"""
    try:
        from prompt_loader import PromptLoader
        
        loader = PromptLoader(
            prompts_dir=config.PROMT_FILES_DIR,
            prompt_files=config.PROMPT_FILES
        )
        
        # Проверяем доступность файлов
        validation = await loader.validate_prompts()
        
        print(f"📝 Статус промптов:")
        for filename, status in validation.items():
            status_icon = "✅" if status else "❌"
            print(f"   {status_icon} {filename}")
        
        # Пробуем загрузить системный промпт
        if any(validation.values()):
            system_prompt = await loader.load_system_prompt()
            print(f"✅ Системный промпт загружен ({len(system_prompt)} символов)")
            
            # Проверяем наличие JSON инструкций
            if "JSON МЕТАДАННЫМ" in system_prompt:
                print("✅ JSON инструкции включены в системный промпт")
            else:
                print("⚠️ JSON инструкции не найдены в системном промпте")
            
            if '"этап":' in system_prompt:
                print("✅ Примеры JSON найдены в промпте")
            else:
                print("⚠️ Примеры JSON не найдены в промпте")
            
            # Проверяем приветственное сообщение
            welcome_message = await loader.load_welcome_message()
            print(f"✅ Приветственное сообщение загружено ({len(welcome_message)} символов)")
            
            # Проверяем справочное сообщение
            help_message = await loader.load_help_message()
            print(f"✅ Справочное сообщение загружено ({len(help_message)} символов)")
            
            return True
        else:
            print("❌ Не удалось загрузить ни одного промпта")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка загрузки промптов: {e}")
        return False

async def check_admin_system(config):
    """Проверяем админскую систему"""
    try:
        print("👑 Проверка админской системы...")
        
        if not config.ADMIN_TELEGRAM_IDS:
            print("⚠️ Админы не настроены (ADMIN_TELEGRAM_IDS пуст)")
            return False
        
        # Проверяем AdminManager
        from admin_manager import AdminManager
        from supabase_client import SupabaseClient
        
        supabase_client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await supabase_client.initialize()
        
        admin_manager = AdminManager(config, supabase_client)
        print(f"✅ AdminManager инициализирован ({len(admin_manager.admin_ids)} админов)")
        
        # Проверяем ConversationManager
        from conversation_manager import ConversationManager
        conversation_manager = ConversationManager(supabase_client, admin_manager)
        print("✅ ConversationManager инициализирован")
        
        # Проверяем AnalyticsManager
        from analytics_manager import AnalyticsManager
        analytics_manager = AnalyticsManager(supabase_client)
        
        # Тестируем получение статистики
        funnel_stats = await analytics_manager.get_funnel_stats(1)
        print("✅ AnalyticsManager работает")
        
        print("✅ Админская система готова к работе")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка админской системы: {e}")
        return False

async def check_json_parsing():
    """Проверяем парсинг JSON метаданных"""
    try:
        print("🧪 Проверка парсинга JSON...")
        
        import json
        
        def parse_ai_response(ai_response: str) -> tuple[str, dict]:
            """Исправленная функция парсинга JSON из quick_json_test.py"""
            try:
                # Метод 1: Ищем последнюю позицию, где начинается JSON с "этап"
                last_etap_pos = ai_response.rfind('"этап"')
                if last_etap_pos == -1:
                    return ai_response, {}
                
                # Ищем открывающую скобку перед "этап"
                json_start = -1
                for i in range(last_etap_pos, -1, -1):
                    if ai_response[i] == '{':
                        json_start = i
                        break
                
                if json_start == -1:
                    return ai_response, {}
                
                # Теперь найдем соответствующую закрывающую скобку
                brace_count = 0
                json_end = -1
                
                for i in range(json_start, len(ai_response)):
                    char = ai_response[i]
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            json_end = i
                            break
                
                if json_end == -1:
                    return ai_response, {}
                
                # Извлекаем JSON и текст ответа
                json_str = ai_response[json_start:json_end + 1]
                response_text = ai_response[:json_start].strip()
                
                try:
                    metadata = json.loads(json_str)
                    return response_text, metadata
                except json.JSONDecodeError:
                    return ai_response, {}
                    
            except Exception:
                return ai_response, {}
        
        # Тестовые случаи
        test_response = '''Отлично! Записал ваш номер телефона.

{
  "этап": "contacts",
  "качество": 9,
  "события": [
    {
      "тип": "телефон",
      "инфо": "Иван Петров +79219603144"
    }
  ]
}'''
        
        response_text, metadata = parse_ai_response(test_response)
        
        if metadata:
            print("✅ JSON успешно распарсен")
            print(f"   Этап: {metadata.get('этап')}")
            print(f"   Качество: {metadata.get('качество')}")
            print(f"   События: {len(metadata.get('события', []))}")
            return True
        else:
            print("❌ Не удалось распарсить JSON")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка парсинга JSON: {e}")
        return False

        
async def check_database_structure():
    """Проверяем структуру базы данных"""
    try:
        print("📊 Проверка структуры БД...")
        
        # Проверяем наличие SQL файлов в корне проекта
        root_dir = Path(__file__).parent
        sql_files = [
            "database_structure.sql",
            "admin_migration.sql"
        ]
        
        for sql_file in sql_files:
            sql_path = root_dir / sql_file
            if sql_path.exists():
                print(f"✅ {sql_file} найден")
            else:
                print(f"❌ {sql_file} не найден")
        
        print("ℹ️ Для проверки таблиц в БД запустите SQL скрипты в Supabase")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка проверки БД: {e}")
        return False

async def check_environment():
    """Проверяем окружение"""
    print("🔧 Проверка окружения...")
    
    # Проверяем наличие .env файла
    env_file = Path(".env")
    if env_file.exists():
        print("✅ Файл .env найден")
    else:
        print("⚠️ Файл .env не найден в текущей директории")
    
    # Проверяем Python зависимости
    dependencies = [
        ('aiogram', 'aiogram'),
        ('supabase', 'supabase'), 
        ('openai', 'openai'),
        ('python-dotenv', 'dotenv'),
        ('aiofiles', 'aiofiles')
    ]
    
    for dep_name, import_name in dependencies:
        try:
            if import_name == 'aiogram':
                import aiogram
                print(f"✅ {dep_name} {aiogram.__version__}")
            elif import_name == 'openai':
                import openai
                print(f"✅ {dep_name} {openai.version.VERSION}")
            else:
                __import__(import_name)
                print(f"✅ {dep_name} установлен")
        except ImportError:
            print(f"❌ {dep_name} не установлен")

async def run_quick_test():
    """Быстрый тест основного функционала"""
    try:
        print("⚡ Быстрый тест компонентов...")
        
        from config import Config
        config = Config()
        
        if config.ADMIN_TELEGRAM_IDS:
            print(f"✅ {len(config.ADMIN_TELEGRAM_IDS)} админов настроено")
        else:
            print("⚠️ Админы не настроены")
        
        # Тест парсинга JSON
        await check_json_parsing()
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка быстрого теста: {e}")
        return False

async def main():
    """Основная функция проверки"""
    # Определяем какого бота проверять
    bot_name = "growthmed-october-24"  # по умолчанию
    if len(sys.argv) > 1:
        bot_name = sys.argv[1]
    
    print(f"🚀 Проверка настройки Telegram Sales Bot v2.0: {bot_name}")
    print(f"🤖 Bot ID будет автоопределен как: {bot_name}\n")
    
    # Настраиваем окружение для бота (автоматически устанавливает BOT_ID)
    config_dir = setup_bot_environment(bot_name)
    if not config_dir:
        return
    
    # Проверяем окружение
    await check_environment()
    print()
    
    # Проверяем конфигурацию
    config = await check_config()
    if not config:
        print("\n❌ Невозможно продолжить без правильной конфигурации")
        return
    print()
    
    # Основные проверки
    checks = [
        ("База данных", check_database_structure()),
        ("Supabase", check_supabase(config)),
        ("OpenAI", check_openai(config)),
        ("Промпты", check_prompts(config)),
        ("Админская система", check_admin_system(config)),
        ("JSON парсинг", check_json_parsing()),
        ("Быстрый тест", run_quick_test())
    ]
    
    results = {}
    for name, check_coro in checks:
        print(f"\n🔍 Проверка: {name}")
        results[name] = await check_coro
    
    # Итоговый результат
    print(f"\n{'='*60}")
    print(f"📋 ИТОГОВЫЙ ОТЧЕТ для {bot_name}:")
    
    all_passed = True
    critical_failed = False
    
    # Критические компоненты
    critical_checks = ["Supabase", "OpenAI", "Промпты"]
    
    for name, passed in results.items():
        if name in critical_checks:
            status = "✅ ПРОЙДЕНА" if passed else "❌ КРИТИЧЕСКАЯ ОШИБКА"
            if not passed:
                critical_failed = True
        else:
            status = "✅ ПРОЙДЕНА" if passed else "⚠️ ПРЕДУПРЕЖДЕНИЕ"
        
        print(f"   {name}: {status}")
        if not passed:
            all_passed = False
    
    print(f"\n📊 Результат: {sum(results.values())}/{len(results)} проверок пройдено")
    
    if critical_failed:
        print("\n🚨 КРИТИЧЕСКИЕ ОШИБКИ! Бот не может быть запущен.")
        print("   Исправьте критические ошибки перед запуском.")
    elif all_passed:
        print("\n🎉 Все проверки пройдены! Бот готов к запуску.")
        print(f"   Запустите: python {bot_name}.py")
        if config.ADMIN_TELEGRAM_IDS:
            print(f"   👑 Админский доступ настроен для: {config.ADMIN_TELEGRAM_IDS}")
    else:
        print("\n⚠️ Есть предупреждения, но бот может работать.")
        print("   Рекомендуется исправить предупреждения для полного функционала.")
    
    if config and config.DEBUG_MODE:
        print("\n🐛 РЕЖИМ ОТЛАДКИ ВКЛЮЧЕН - JSON будет показываться пользователям")
    
    print(f"{'='*60}")

if __name__ == "__main__":
    asyncio.run(main())