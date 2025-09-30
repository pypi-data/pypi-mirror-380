# Исправленный скрипт для диагностики проблемы с таймаутом диалогов

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

async def debug_timeout_issue():
    """Диагностирует проблему с таймаутом диалогов"""
    
    print("🔍 Диагностика проблемы с таймаутом диалогов\n")
    
    # Определяем какого бота диагностировать
    bot_name = "growthmed-october-24"  # по умолчанию
    if len(sys.argv) > 1:
        bot_name = sys.argv[1]
    
    print(f"🚀 Диагностика для бота: {bot_name}")
    print(f"🤖 Bot ID будет автоопределен как: {bot_name}\n")
    
    # Настраиваем окружение для бота (автоматически устанавливает BOT_ID)
    config_dir = setup_bot_environment(bot_name)
    if not config_dir:
        return
    
    # Теперь импортируем модули ПОСЛЕ настройки окружения
    from config import Config
    from supabase_client import SupabaseClient
    
    # 1. Проверяем конфигурацию
    config = Config()
    print(f"📋 Конфигурация:")
    print(f"   BOT_ID: {config.BOT_ID}")
    print(f"   ADMIN_SESSION_TIMEOUT_MINUTES: {config.ADMIN_SESSION_TIMEOUT_MINUTES}")
    print(f"   PROMT_FILES_DIR: {config.PROMT_FILES_DIR}")
    print(f"   Найдено промпт-файлов: {len(config.PROMPT_FILES)}")
    print()
    
    # 2. Проверяем часовые пояса
    print(f"🕐 Временные зоны:")
    now_naive = datetime.now()
    now_utc = datetime.now(timezone.utc)
    print(f"   datetime.now() (локальное): {now_naive}")
    print(f"   datetime.now(timezone.utc): {now_utc}")
    print(f"   Разница: {(now_naive.replace(tzinfo=timezone.utc) - now_utc).total_seconds() / 3600:.1f} часов")
    print()
    
    # 3. Проверяем активные диалоги в БД
    try:
        supabase_client = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
        await supabase_client.initialize()
        
        response = supabase_client.client.table('admin_user_conversations').select(
            'id', 'admin_id', 'user_id', 'started_at', 'auto_end_at'
        ).eq('status', 'active').execute()
        
        conversations = response.data
        
        print(f"📊 Активные диалоги в БД: {len(conversations)}")
        
        for i, conv in enumerate(conversations, 1):
            print(f"\n{i}. Диалог ID: {conv['id']}")
            print(f"   Админ: {conv['admin_id']}, Пользователь: {conv['user_id']}")
            
            # Парсим времена
            started_at = conv['started_at']
            auto_end_at = conv['auto_end_at']
            
            print(f"   started_at (сырое): {started_at}")
            print(f"   auto_end_at (сырое): {auto_end_at}")
            
            try:
                # Парсим как делает код
                if started_at.endswith('Z'):
                    start_time = datetime.fromisoformat(started_at.replace('Z', '+00:00'))
                elif '+' in started_at or started_at.count(':') >= 3:
                    start_time = datetime.fromisoformat(started_at)
                else:
                    naive_time = datetime.fromisoformat(started_at)
                    start_time = naive_time.replace(tzinfo=timezone.utc)
                
                if auto_end_at.endswith('Z'):
                    end_time = datetime.fromisoformat(auto_end_at.replace('Z', '+00:00'))
                elif '+' in auto_end_at or auto_end_at.count(':') >= 3:
                    end_time = datetime.fromisoformat(auto_end_at)
                else:
                    naive_time = datetime.fromisoformat(auto_end_at)
                    end_time = naive_time.replace(tzinfo=timezone.utc)
                
                print(f"   start_time (парсед): {start_time}")
                print(f"   end_time (парсед): {end_time}")
                
                # Вычисляем длительность диалога
                planned_duration = end_time - start_time
                planned_minutes = int(planned_duration.total_seconds() / 60)
                print(f"   Запланированная длительность: {planned_minutes} минут")
                
                # Проверяем соответствие конфигу
                expected = config.ADMIN_SESSION_TIMEOUT_MINUTES
                if planned_minutes == expected:
                    print(f"   ✅ Соответствует конфигу ({expected} мин)")
                else:
                    print(f"   ❌ НЕ соответствует конфигу! Ожидалось {expected} мин, получили {planned_minutes} мин")
                
                # Вычисляем текущее время до автозавершения
                now_utc = datetime.now(timezone.utc)
                
                # Приводим к UTC
                if end_time.tzinfo != timezone.utc:
                    end_time_utc = end_time.astimezone(timezone.utc)
                else:
                    end_time_utc = end_time
                
                remaining = end_time_utc - now_utc
                remaining_minutes = max(0, int(remaining.total_seconds() / 60))
                
                print(f"   now_utc: {now_utc}")
                print(f"   end_time_utc: {end_time_utc}")
                print(f"   Оставшееся время: {remaining_minutes} минут")
                
                # Вычисляем сколько уже прошло
                if start_time.tzinfo != timezone.utc:
                    start_time_utc = start_time.astimezone(timezone.utc)
                else:
                    start_time_utc = start_time
                    
                elapsed = now_utc - start_time_utc
                elapsed_minutes = max(0, int(elapsed.total_seconds() / 60))
                print(f"   Прошло времени: {elapsed_minutes} минут")
                
                # Проверяем математику
                total_check = elapsed_minutes + remaining_minutes
                print(f"   Проверка: {elapsed_minutes} + {remaining_minutes} = {total_check} мин (должно быть ~{planned_minutes})")
                
                if abs(total_check - planned_minutes) > 2:
                    print(f"   ⚠️ ПРОБЛЕМА: сумма не сходится! Возможная проблема с timezone")
                
            except Exception as e:
                print(f"   ❌ Ошибка парсинга времени: {e}")
        
        if not conversations:
            print("   Нет активных диалогов для анализа")
            print("   💡 Создайте диалог командой /чат USER_ID для тестирования")
            
    except Exception as e:
        print(f"❌ Ошибка подключения к БД: {e}")

async def test_conversation_creation():
    """Тестирует создание нового диалога с правильным таймаутом"""
    print(f"\n{'='*50}")
    print("🧪 ТЕСТ СОЗДАНИЯ ДИАЛОГА")
    print(f"{'='*50}")
    
    from config import Config
    from supabase_client import SupabaseClient
    from datetime import timedelta
    
    config = Config()
    timeout_minutes = config.ADMIN_SESSION_TIMEOUT_MINUTES
    
    print(f"📋 Конфигурация таймаута: {timeout_minutes} минут")
    
    # Эмулируем создание диалога
    now_utc = datetime.now(timezone.utc)
    auto_end_utc = now_utc + timedelta(minutes=timeout_minutes)
    
    print(f"🕐 now_utc: {now_utc}")
    print(f"⏰ auto_end_utc: {auto_end_utc}")
    print(f"📏 Разница: {int((auto_end_utc - now_utc).total_seconds() / 60)} минут")
    
    # Проверяем ISO формат
    auto_end_iso = auto_end_utc.isoformat()
    print(f"📝 ISO формат: {auto_end_iso}")
    
    # Проверяем парсинг обратно
    try:
        if auto_end_iso.endswith('Z'):
            parsed_back = datetime.fromisoformat(auto_end_iso.replace('Z', '+00:00'))
        elif '+' in auto_end_iso:
            parsed_back = datetime.fromisoformat(auto_end_iso)
        else:
            parsed_back = datetime.fromisoformat(auto_end_iso).replace(tzinfo=timezone.utc)
        
        print(f"🔄 Парсед обратно: {parsed_back}")
        
        # Проверяем что время совпадает
        if abs((parsed_back - auto_end_utc).total_seconds()) < 1:
            print("✅ Парсинг работает корректно")
        else:
            print("❌ Проблема с парсингом времени")
            
    except Exception as e:
        print(f"❌ Ошибка парсинга: {e}")

if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')
    
    async def main():
        await debug_timeout_issue()
        await test_conversation_creation()
    
    asyncio.run(main())