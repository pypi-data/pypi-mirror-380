# Обновленная запускалка (например growthmed-october-24.py)

import os
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv

# 🆕 Автоматически определяем имя бота из имени файла запускалки
script_name = Path(__file__).stem  
print(f"🔍 Определен Bot ID из имени файла: {script_name}")

root_dir = Path(__file__).parent

# 🔄 ВАЖНО: Добавляем корневую директорию в sys.path перед всеми импортами
sys.path.insert(0, str(root_dir))

# 🆕 КРИТИЧЕСКИ ВАЖНО: Устанавливаем BOT_ID ДО загрузки .env и импорта config
os.environ['BOT_ID'] = script_name
print(f"🤖 BOT_ID установлен: {script_name}")

# Устанавливаем рабочую директорию в папку конфигурации
config_dir = root_dir / 'configs' / script_name
print(f"🔍 Папка конфигурации: {config_dir}")

if not config_dir.exists():
    print(f"❌ Папка конфигурации не найдена: {config_dir}")
    print(f"   Создайте папку или используйте команду:")
    print(f"   python create_bot.py имя-шаблона {script_name}")
    exit(1)

# Загружаем .env ДО смены директории и импорта config
env_file = config_dir / '.env'
if env_file.exists():
    print(f"🔧 Загружаем .env из: {env_file}")
    load_dotenv(env_file)
else:
    print(f"❌ Файл .env не найден: {env_file}")
    print(f"   Создайте файл .env в папке {config_dir}")
    exit(1)

# 🔄 Меняем директорию ПОСЛЕ загрузки .env но ДО импорта модулей
os.chdir(str(config_dir))

# 🔄 Импортируем main из корневой директории
try:
    from main import main
    print(f"✅ Модули успешно импортированы")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print(f"📁 Текущая директория: {os.getcwd()}")
    print(f"📁 Пути Python: {sys.path[:3]}...")
    exit(1)

if __name__ == "__main__":
    print(f"🚀 Запуск бота {script_name.upper()} с автоопределенным BOT_ID = {script_name}")
    print(f"📁 Рабочая директория: {os.getcwd()}")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n⏹️ Бот {script_name} остановлен пользователем")
    except Exception as e:
        print(f"\n💥 Критическая ошибка бота {script_name}: {e}")
        exit(1)