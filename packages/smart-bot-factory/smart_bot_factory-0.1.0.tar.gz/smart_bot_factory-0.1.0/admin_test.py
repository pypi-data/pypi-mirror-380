#!/usr/bin/env python3
"""
Утилита для тестирования системы администрирования бота
Запуск: 
  python admin_test.py                           # для growthmed-october-24 (по умолчанию)
  python admin_test.py growthmed-october-24      # явно указать бота
  python admin_test.py другой-бот               # для других ботов
"""

import asyncio
import logging
import json
import re
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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


async def test_config():
    """Тестирует конфигурацию с админскими настройками"""
    try:
        from config import Config
        config = Config()
        
        print("✅ Конфигурация загружена")
        print(f"👥 Админов настроено: {len(config.ADMIN_TELEGRAM_IDS)}")
        print(f"🐛 Режим отладки: {'Включен' if config.DEBUG_MODE else 'Выключен'}")
        
        if config.ADMIN_TELEGRAM_IDS:
            print(f"📋 ID админов: {config.ADMIN_TELEGRAM_IDS}")
        else:
            print("⚠️ Админы не настроены!")
        
        return config
    except Exception as e:
        print(f"❌ Ошибка конфигурации: {e}")
        return None

async def test_database_migration():
    """Проверяет выполнение миграции БД"""
    try:
        from supabase_client import SupabaseClient
        from config import Config
        
        config = Config()
        client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await client.initialize()
        
        # Проверяем новые таблицы
        tables_to_check = [
            'sales_admins',
            'admin_user_conversations', 
            'session_events'
        ]
        
        for table in tables_to_check:
            try:
                response = client.client.table(table).select('*').limit(1).execute()
                print(f"✅ Таблица {table} существует")
            except Exception as e:
                print(f"❌ Таблица {table} не найдена: {e}")
        
        # Проверяем новые колонки
        try:
            response = client.client.table('sales_chat_sessions').select(
                'current_stage', 'lead_quality_score'
            ).limit(1).execute()
            print("✅ Новые колонки в sales_chat_sessions добавлены")
        except Exception as e:
            print(f"❌ Новые колонки не найдены: {e}")
        
        try:
            response = client.client.table('sales_messages').select('ai_metadata').limit(1).execute()
            print("✅ Колонка ai_metadata в sales_messages добавлена")
        except Exception as e:
            print(f"❌ Колонка ai_metadata не найдена: {e}")
        
        print("✅ Проверка БД завершена")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка проверки БД: {e}")
        return False

async def test_admin_manager():
    """Тестирует AdminManager"""
    try:
        from admin_manager import AdminManager
        from supabase_client import SupabaseClient
        from config import Config
        
        config = Config()
        supabase_client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await supabase_client.initialize()
        
        admin_manager = AdminManager(config, supabase_client)
        await admin_manager.sync_admins_from_config()
        
        # Тестируем функции
        if config.ADMIN_TELEGRAM_IDS:
            test_admin_id = config.ADMIN_TELEGRAM_IDS[0]
            
            print(f"✅ Админ {test_admin_id}: {admin_manager.is_admin(test_admin_id)}")
            print(f"✅ В режиме админа: {admin_manager.is_in_admin_mode(test_admin_id)}")
            
            # Тестируем переключение режима
            new_mode = admin_manager.toggle_admin_mode(test_admin_id)
            print(f"✅ Режим переключен на: {'админ' if new_mode else 'пользователь'}")
            
            # Возвращаем обратно
            admin_manager.toggle_admin_mode(test_admin_id)
        
        stats = admin_manager.get_stats()
        print(f"✅ Статистика админов: {stats}")
        
        print("✅ AdminManager работает корректно")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка AdminManager: {e}")
        return False

def test_json_parsing():
    """Тестирует парсинг JSON из ответов ИИ"""
    print("\n🧪 Тестирование парсинга JSON...")
    
    test_cases = [
        {
            "name": "Корректный JSON",
            "response": '''Отлично! Записал ваш номер телефона.

{
  "этап": "contacts",
  "качество": 9,
  "события": [
    {
      "тип": "телефон",
      "инфо": "Иван Петров +79219603144"
    }
  ]
}''',
            "should_succeed": True
        },
        {
            "name": "JSON без событий", 
            "response": '''Расскажу подробнее о конференции...

{
  "этап": "consult",
  "качество": 6,
  "события": []
}''',
            "should_succeed": True
        },
        {
            "name": "Ответ без JSON",
            "response": "Простой ответ без метаданных",
            "should_succeed": False
        },
        {
            "name": "Невалидный JSON",
            "response": '''Ответ с плохим JSON

{
  "этап": "consult",
  "качество": 6,
  события": []
}''',
            "should_succeed": False
        }
    ]
    
    def parse_ai_response(ai_response: str) -> tuple[str, dict]:
        """Правильная функция парсинга JSON"""
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
                # Fallback метод
                return parse_ai_response_fallback(ai_response)
                
        except Exception:
            return parse_ai_response_fallback(ai_response)
    
    def parse_ai_response_fallback(ai_response: str) -> tuple[str, dict]:
        """Резервный метод парсинга JSON"""
        try:
            lines = ai_response.strip().split('\n')
            
            # Ищем строку с "этап"
            etap_line = -1
            for i, line in enumerate(lines):
                if '"этап"' in line:
                    etap_line = i
                    break
            
            if etap_line == -1:
                return ai_response, {}
            
            # Ищем начало JSON
            json_start_line = -1
            for i in range(etap_line, -1, -1):
                if lines[i].strip().startswith('{'):
                    json_start_line = i
                    break
            
            if json_start_line == -1:
                return ai_response, {}
            
            # Ищем конец JSON (балансируем скобки)
            brace_count = 0
            json_end_line = -1
            
            for i in range(json_start_line, len(lines)):
                line = lines[i]
                for char in line:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            json_end_line = i
                            break
                if json_end_line != -1:
                    break
            
            if json_end_line == -1:
                return ai_response, {}
            
            # Собираем JSON
            json_lines = lines[json_start_line:json_end_line + 1]
            json_str = '\n'.join(json_lines)
            
            # Собираем текст ответа
            response_lines = lines[:json_start_line]
            response_text = '\n'.join(response_lines).strip()
            
            try:
                metadata = json.loads(json_str)
                return response_text, metadata
            except json.JSONDecodeError:
                return ai_response, {}
                
        except Exception:
            return ai_response, {}
    
    success_count = 0
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nТест {i}: {test_case['name']}")
        
        response_text, metadata = parse_ai_response(test_case['response'])
        has_metadata = bool(metadata)
        
        if has_metadata == test_case['should_succeed']:
            print("✅ ПРОЙДЕН")
            if has_metadata:
                print(f"   Этап: {metadata.get('этап', 'N/A')}")
                print(f"   Качество: {metadata.get('качество', 'N/A')}")
                print(f"   События: {len(metadata.get('события', []))}")
            success_count += 1
        else:
            print("❌ ПРОВАЛЕН")
            print(f"   Ожидался JSON: {test_case['should_succeed']}")
            print(f"   Получен JSON: {has_metadata}")
    
    print(f"\n📊 Результат: {success_count}/{len(test_cases)} тестов пройдено")
    return success_count == len(test_cases)

async def test_prompt_loader():
    """Тестирует PromptLoader с JSON инструкциями"""
    try:
        from prompt_loader import PromptLoader
        from config import Config
        
        config = Config()
        loader = PromptLoader(config.PROMT_FILES_DIR, config.PROMPT_FILES)
        
        # Тестируем загрузку системного промпта
        system_prompt = await loader.load_system_prompt()
        
        # Проверяем наличие JSON инструкций
        if "JSON МЕТАДАННЫМ" in system_prompt:
            print("✅ JSON инструкции включены в системный промпт")
        else:
            print("❌ JSON инструкции не найдены в системном промпте")
        
        if '"этап":' in system_prompt:
            print("✅ Примеры JSON найдены в промпте")
        else:
            print("❌ Примеры JSON не найдены в промпте")
        
        # Тестируем валидацию
        validation = await loader.validate_prompts()
        print(f"✅ Валидация промптов: {validation}")
        
        # Тестируем функцию парсинга JSON (если есть)
        if hasattr(loader, 'test_json_parsing'):
            test_response = '''Тестовый ответ

{
  "этап": "test",
  "качество": 5,
  "события": []
}'''
            
            parse_result = await loader.test_json_parsing(test_response)
            if parse_result['success']:
                print("✅ Тестирование парсинга JSON успешно")
            else:
                print(f"❌ Ошибка парсинга JSON: {parse_result['error']}")
        
        print("✅ PromptLoader работает корректно")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка PromptLoader: {e}")
        return False

async def test_analytics():
    """Тестирует AnalyticsManager"""
    try:
        from analytics_manager import AnalyticsManager
        from supabase_client import SupabaseClient
        from config import Config
        
        config = Config()
        supabase_client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await supabase_client.initialize()
        
        analytics = AnalyticsManager(supabase_client)
        
        # Тестируем получение статистики
        funnel_stats = await analytics.get_funnel_stats(7)
        print(f"✅ Статистика воронки получена: {funnel_stats}")
        
        events_stats = await analytics.get_events_stats(7)
        print(f"✅ Статистика событий получена: {events_stats}")
        
        # Тестируем форматирование
        formatted_funnel = analytics.format_funnel_stats(funnel_stats)
        print("✅ Форматирование статистики работает")
        
        daily_summary = await analytics.get_daily_summary()
        print("✅ Дневная сводка получена")
        
        print("✅ AnalyticsManager работает корректно")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка AnalyticsManager: {e}")
        return False

async def run_all_tests():
    """Запускает все тесты"""
    # Определяем какого бота тестировать
    bot_name = "growthmed-october-24"  # по умолчанию
    if len(sys.argv) > 1:
        bot_name = sys.argv[1]
    
    print(f"🚀 Запуск тестов системы администрирования для {bot_name}")
    print(f"🤖 Bot ID будет автоопределен как: {bot_name}\n")
    
    # Настраиваем окружение для бота (автоматически устанавливает BOT_ID)
    config_dir = setup_bot_environment(bot_name)
    if not config_dir:
        return
    
    tests = [
        ("Конфигурация", test_config()),
        ("База данных", test_database_migration()),
        ("AdminManager", test_admin_manager()),
        ("JSON парсинг", test_json_parsing()),
        ("PromptLoader", test_prompt_loader()),
        ("Analytics", test_analytics())
    ]
    
    results = []
    for test_name, test_coro in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        
        if asyncio.iscoroutine(test_coro):
            result = await test_coro
        else:
            result = test_coro
            
        results.append((test_name, result))
    
    # Итоговый отчет
    print(f"\n{'='*50}")
    print(f"📋 ИТОГОВЫЙ ОТЧЕТ для {bot_name}:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
        print(f"   {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n📊 Результат: {passed}/{len(results)} тестов пройдено")
    
    if passed == len(results):
        print("🎉 Все тесты пройдены! Система готова к работе.")
        print(f"   Запустите: python {bot_name}.py")
    else:
        print("⚠️ Есть проблемы, которые нужно исправить.")
    
    print(f"{'='*50}")

if __name__ == "__main__":
    asyncio.run(run_all_tests())