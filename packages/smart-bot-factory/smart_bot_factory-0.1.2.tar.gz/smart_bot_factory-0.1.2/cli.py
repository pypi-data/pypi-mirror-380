"""
CLI интерфейс для Smart Bot Factory
"""

import os
import sys
import click
import subprocess
import shutil
from pathlib import Path

from project_root_finder import root

PROJECT_ROOT = root

@click.group()
def cli():
    """Smart Bot Factory - инструмент для создания умных чат-ботов"""
    pass

@cli.command()
@click.argument("bot_id")
@click.argument("template", required=False, default="base")
def create(bot_id: str, template: str = "base"):
    """Создать нового бота"""
    success = create_new_bot_structure(template, bot_id)
    if not success:
        sys.exit(1)

@cli.command()
def list():
    """Показать список доступных ботов"""
    bots = list_bots_in_bots_folder()
    if not bots:
        click.echo("Нет доступных ботов")
        return
        
    click.echo("Доступные боты:")
    for bot in sorted(bots):
        click.echo(f"  - {bot}")

@cli.command()
@click.argument("bot_id")
def run(bot_id: str):
    """Запустить бота"""
    try:
        # Проверяем существование бота
        bot_path = PROJECT_ROOT / Path("bots") / bot_id
        if not bot_path.exists():
            raise click.ClickException(f"Бот {bot_id} не найден в папке bots/")
        
        # Проверяем наличие основного файла бота в корневой директории
        bot_file = PROJECT_ROOT / Path(f"{bot_id}.py")
        if not bot_file.exists():
            raise click.ClickException(f"Файл {bot_id}.py не найден в корневой директории")
        
        # Проверяем наличие .env файла
        env_file = bot_path / ".env"
        if not env_file.exists():
            raise click.ClickException(f"Файл .env не найден для бота {bot_id}")
        
        # Настраиваем окружение для бота
        from dotenv import load_dotenv
        
        # Добавляем корень проекта в sys.path
        sys.path.insert(0, str(PROJECT_ROOT))
        
        # Загружаем .env файл
        load_dotenv(env_file)
        click.echo(f"Загружен .env файл: {env_file}")
        
        # Устанавливаем переменные окружения
        os.environ["BOT_ID"] = bot_id
        
        # Устанавливаем путь к промптам
        prompts_dir = bot_path / "prompts"
        if prompts_dir.exists():
            os.environ["PROMT_FILES_DIR"] = str(prompts_dir)
            click.echo(f"Установлен путь к промптам: {prompts_dir}")
        
        # Запускаем бота из корневой директории
        click.echo(f"Запускаем бота {bot_id}...")
        subprocess.run([sys.executable, str(bot_file)], check=True, cwd=str(PROJECT_ROOT))
        
    except subprocess.CalledProcessError as e:
        click.echo(f"Ошибка при запуске бота: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Ошибка: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("bot_id")
@click.option("--file", help="Запустить тесты только из указанного файла")
@click.option("-v", "--verbose", is_flag=True, help="Подробный вывод")
@click.option("--max-concurrent", default=5, help="Максимальное количество потоков")
def test(bot_id: str, file: str = None, verbose: bool = False, max_concurrent: int = 5):
    """Запустить тесты бота"""
    try:        
        # Проверяем существование бота
        bot_path = PROJECT_ROOT / "bots" / bot_id
        if not bot_path.exists():
            raise click.ClickException(f"Бот {bot_id} не найден в папке {PROJECT_ROOT}/bots/")
        
        # Проверяем наличие тестов
        tests_dir = bot_path / "tests"
        if not tests_dir.exists():
            click.echo(f"⚠️ Тесты не найдены для бота {bot_id}")
            return
        
        # Ищем YAML файлы с тестами
        yaml_files = [str(f.name) for f in tests_dir.glob("*.yaml")]
        
        if not yaml_files:
            click.echo(f"⚠️ YAML тесты не найдены для бота {bot_id}")
            return
        
        click.echo(f"Запускаем тесты для бота {bot_id}...")
        
        # Формируем команду для запуска
        bot_testing_path = Path(__file__).parent / "creation" / "bot_testing.py"
        cmd = [sys.executable, str(bot_testing_path), bot_id]
        
        if file:
            cmd.append(file)
        
        if verbose:
            cmd.append("-v")
        
        if max_concurrent != 5:
            cmd.extend(["--max-concurrent", str(max_concurrent)])
        
        # Запускаем тесты
        result = subprocess.run(cmd, check=False)
        
        if result.returncode == 0:
            click.echo("✅ Все тесты пройдены")
        else:
            click.echo("❌ Есть ошибки в тестах")
            sys.exit(1)
            
    except subprocess.CalledProcessError as e:
        click.echo(f"Ошибка при запуске тестов: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Ошибка: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("bot_id")
def config(bot_id: str):
    """Настроить конфигурацию бота"""
    try:
        # Проверяем существование бота
        bot_path = PROJECT_ROOT / Path("bots") / bot_id
        if not bot_path.exists():
            raise click.ClickException(f"Бот {bot_id} не найден в папке bots/")
        
        # Открываем .env файл в редакторе
        env_file = bot_path / ".env"
        if not env_file.exists():
            raise click.ClickException(f"Файл .env не найден для бота {bot_id}")
        
        # Определяем редактор
        editor = os.environ.get('EDITOR', 'notepad' if os.name == 'nt' else 'nano')
        
        click.echo(f"Открываем конфигурацию бота {bot_id}...")
        subprocess.run([editor, str(env_file)], check=True)
        
    except subprocess.CalledProcessError as e:
        click.echo(f"Ошибка при открытии редактора: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Ошибка: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("bot_id")
@click.option("--list", "list_prompts", is_flag=True, help="Показать список промптов")
@click.option("--edit", "edit_prompt", help="Редактировать промпт")
@click.option("--add", "add_prompt", help="Добавить новый промпт")
def prompts(bot_id: str, list_prompts: bool = False, edit_prompt: str = None, add_prompt: str = None):
    """Управление промптами бота"""
    try:
        # Проверяем существование бота
        bot_path = PROJECT_ROOT / Path("bots") / bot_id
        if not bot_path.exists():
            raise click.ClickException(f"Бот {bot_id} не найден в папке bots/")
        
        prompts_dir = bot_path / "prompts"
        if not prompts_dir.exists():
            raise click.ClickException(f"Папка промптов не найдена для бота {bot_id}")
        
        if list_prompts:
            # Показываем список промптов
            prompt_files = [f.name for f in prompts_dir.glob("*.txt")]
            
            if not prompt_files:
                click.echo("Промпты не найдены")
                return
            
            click.echo(f"Промпты бота {bot_id}:")
            for prompt_file in sorted(prompt_files):
                click.echo(f"  - {prompt_file[:-4]}")
        
        elif edit_prompt:
            # Редактируем промпт
            prompt_file = prompts_dir / f"{edit_prompt}.txt"
            if not prompt_file.exists():
                raise click.ClickException(f"Промпт {edit_prompt} не найден")
            
            editor = os.environ.get('EDITOR', 'notepad' if os.name == 'nt' else 'nano')
            click.echo(f"Редактируем промпт {edit_prompt}...")
            subprocess.run([editor, str(prompt_file)], check=True)
        
        elif add_prompt:
            # Добавляем новый промпт
            prompt_file = prompts_dir / f"{add_prompt}.txt"
            if prompt_file.exists():
                raise click.ClickException(f"Промпт {add_prompt} уже существует")
            
            # Создаем файл с базовым содержимым
            prompt_file.write_text(
                f"# Промпт: {add_prompt}\n\n"
                "Введите содержимое промпта здесь...",
                encoding='utf-8'
            )
            
            # Открываем в редакторе
            editor = os.environ.get('EDITOR', 'notepad' if os.name == 'nt' else 'nano')
            click.echo(f"📝 Создаем новый промпт {add_prompt}...")
            subprocess.run([editor, str(prompt_file)], check=True)
        
        else:
            # Показываем справку
            click.echo("Использование:")
            click.echo("  sbf prompts <bot_id> --list                    # Показать список промптов")
            click.echo("  sbf prompts <bot_id> --edit <prompt_name>      # Редактировать промпт")
            click.echo("  sbf prompts <bot_id> --add <prompt_name>       # Добавить новый промпт")
            
    except subprocess.CalledProcessError as e:
        click.echo(f"Ошибка при открытии редактора: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Ошибка: {e}", err=True)
        sys.exit(1)
        
@cli.command()
def path():
    """Показать путь к проекту"""
    click.echo(PROJECT_ROOT)

@cli.command()
@click.argument("bot_id")
@click.option("--force", "-f", is_flag=True, help="Удалить без подтверждения")
def rm(bot_id: str, force: bool = False):
    """Удалить бота и все его файлы"""
    try:
        # Проверяем существование бота
        bot_path = PROJECT_ROOT / Path("bots") / bot_id
        if not bot_path.exists():
            raise click.ClickException(f"Бот {bot_id} не найден в папке bots/")
        
        # Проверяем наличие основного файла бота в корневой директории
        bot_file = Path(f"{bot_id}.py")
        if not bot_file.exists():
            raise click.ClickException(f"Файл {bot_id}.py не найден в корневой директории")
        
        # Показываем что будет удалено
        click.echo("Будет удалено:")
        click.echo(f"  - Файл запускалки: {bot_file}")
        click.echo(f"  - Папка бота: {bot_path}")
        
        # Запрашиваем подтверждение если не указан --force
        if not force:
            if not click.confirm(f"Вы уверены, что хотите удалить бота {bot_id}?"):
                click.echo("Удаление отменено")
                return
        
        # Удаляем файл запускалки
        if bot_file.exists():
            bot_file.unlink()
            click.echo(f"Файл {bot_file} удален")
        
        # Удаляем папку бота
        if bot_path.exists():
            import shutil
            shutil.rmtree(bot_path)
            click.echo(f"Папка {bot_path} удалена")
        
        click.echo(f"Бот {bot_id} полностью удален")
        
    except Exception as e:
        click.echo(f"Ошибка при удалении бота: {e}", err=True)
        sys.exit(1)
        

@cli.command()
def link():
    """Создать UTM-ссылку для бота"""
    try:
        # Проверяем наличие скрипта генерации ссылок
        link_script = Path("utm_link_generator.py")
        if not link_script.exists():
            raise click.ClickException("Скрипт utm_link_generator.py не найден")
        
        # Запускаем ваш скрипт генерации ссылок
        click.echo("Запускаем генератор UTM-ссылок...")
        subprocess.run([sys.executable, "utm_link_generator.py"], check=True)
        
    except subprocess.CalledProcessError as e:
        click.echo(f"Ошибка при запуске генератора ссылок: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Ошибка: {e}", err=True)
        sys.exit(1)

def create_new_bot_structure(template: str, bot_id: str) -> bool:
    """Создает новую структуру бота в папке bots/"""
    try:
        # Создаем папку bots если её нет
        bots_dir = PROJECT_ROOT / Path("bots")
        bots_dir.mkdir(exist_ok=True)
        
        # Создаем папку для нового бота
        bot_dir = bots_dir / bot_id
        if bot_dir.exists():
            click.echo(f"Бот {bot_id} уже существует")
            return False
        
        bot_dir.mkdir()
        
        # Создаем структуру папок
        (bot_dir / "prompts").mkdir()
        (bot_dir / "tests").mkdir()
        (bot_dir / "reports").mkdir()
        (bot_dir / "welcome_files").mkdir()
        
        if template == "base":
            # Используем growthmed-october-24 как базовый шаблон
            copy_from_growthmed_template(bot_dir, bot_id)
        else:
            # Используем другой шаблон из папки bots
            copy_from_bot_template(template, bot_dir, bot_id)
        
        click.echo(f"Бот {bot_id} создан в папке bots/{bot_id}/")
        click.echo(f"Не забудьте настроить .env файл перед запуском")
        return True
        
    except Exception as e:
        click.echo(f"Ошибка при создании бота: {e}")
        return False

def list_bots_in_bots_folder() -> list:
    """Возвращает список ботов из папки bots/"""
    bots_dir = PROJECT_ROOT / Path("bots")
    if not bots_dir.exists():
        return []
    
    bots = []
    for item in bots_dir.iterdir():
        if item.is_dir() and Path(f"{item.name}.py").exists():
            bots.append(item.name)
    
    return bots

def create_bot_template(bot_id: str) -> str:
    """Создает шаблон основного файла бота"""
    return f'''#!/usr/bin/env python3
"""
Бот {bot_id} - создан с помощью Smart Bot Factory
"""

import asyncio
import sys
import os
from pathlib import Path

# Добавляем корень проекта в путь
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Устанавливаем переменные окружения ДО импорта библиотеки
bot_id = "{bot_id}"
config_dir = Path("bots") / bot_id
prompts_dir = config_dir / "prompts"

if prompts_dir.exists():
    os.environ["PROMT_FILES_DIR"] = str(prompts_dir)
    print(f"📁 Установлен путь к промптам: {{prompts_dir}}")

# Загружаем .env файл ДО импорта библиотеки
env_file = config_dir / ".env"
if env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(env_file)
    print(f"📄 Загружен .env файл: {{env_file}}")
else:
    print(f"⚠️ .env файл не найден: {{env_file}}")

from smart_bot_factory import (
    BotBuilder,
    event_handler,
    schedule_task,
    send_message_by_human,
    send_message_by_ai
)

# =============================================================================
# ОБРАБОТЧИКИ СОБЫТИЙ
# =============================================================================

@event_handler("example_event", "Пример обработчика события")
async def handle_example_event(user_id: int, event_data: dict):
    """Пример обработчика события"""
    # Отправляем подтверждение пользователю
    await send_message_by_human(
        user_id=user_id,
        message_text="✅ Событие обработано!"
    )
    
    return {{
        "status": "success",
        "message": "Событие обработано"
    }}

# =============================================================================
# ЗАПЛАНИРОВАННЫЕ ЗАДАЧИ
# =============================================================================

@schedule_task("example_task", "Пример запланированной задачи")
async def example_task(user_id: int, message: str):
    """Пример запланированной задачи"""
    # Отправляем сообщение
    await send_message_by_human(
        user_id=user_id,
        message_text=f"🔔 Напоминание: {{message}}"
    )
    
    return {{
        "status": "sent",
        "user_id": user_id,
        "message": message
    }}

# =============================================================================
# ОСНОВНАЯ ФУНКЦИЯ
# =============================================================================

async def main():
    """Основная функция запуска бота"""
    try:
        # Создаем и собираем бота
        bot_builder = BotBuilder("{bot_id}")
        await bot_builder.build()
        
        # Запускаем бота
        await bot_builder.start()
        
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {{e}}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
'''

def create_env_template(bot_id: str) -> str:
    """Создает шаблон .env файла"""
    return f'''# Telegram
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

# OpenAI
OPENAI_API_KEY=sk-your-openai-api-key
OPENAI_MODEL=gpt-5-mini
OPENAI_MAX_TOKENS=1500
OPENAI_TEMPERATURE=0.7

# Промпты (каталог)
PROMT_FILES_DIR=prompts

# Файл после приветствия с подписью (если он есть - грузим его в папку welcome_file, если нет - ничего не делаем)
WELCOME_FILE_URL=welcome_files/
WELCOME_FILE_MSG=welcome_file_msg.txt

# 🆕 Администраторы (через запятую)
# Укажите Telegram ID админов
ADMIN_TELEGRAM_IDS=123456789,987654321
ADMIN_SESSION_TIMEOUT_MINUTES=30

# 🆕 Режим отладки (показывать JSON пользователям)
DEBUG_MODE=false

# Дополнительные настройки
MAX_CONTEXT_MESSAGES=50
LOG_LEVEL=INFO
MESSAGE_PARSE_MODE=Markdown

# Настройки продаж
LEAD_QUALIFICATION_THRESHOLD=7
SESSION_TIMEOUT_HOURS=24

# ⚠️ ВАЖНО: BOT_ID теперь НЕ нужен в .env!
# Bot ID автоматически определяется из имени файла запускалки
# Например: python {bot_id}.py → BOT_ID = {bot_id}
'''

def copy_from_growthmed_template(bot_dir: Path, bot_id: str):
    """Копирует шаблон из growthmed-october-24"""
    try:
        # Создаем основной файл бота в корневой директории проекта
        bot_file = PROJECT_ROOT / Path(f"{bot_id}.py")
        bot_file.write_text(create_bot_template(bot_id), encoding='utf-8')
        
        # Копируем .env файл в папку бота
        env_file = bot_dir / ".env"
        env_file.write_text(create_env_template(bot_id), encoding='utf-8')
        
        # Копируем промпты из growthmed-october-24
        source_prompts = Path("configs/growthmed-october-24/prompts")
        target_prompts = bot_dir / "prompts"
        
        if source_prompts.exists():
            for prompt_file in source_prompts.glob("*.txt"):
                shutil.copy2(prompt_file, target_prompts / prompt_file.name)
            click.echo("Промпты скопированы из growthmed-october-24")
        else:
            # Fallback к базовым промптам
            create_basic_prompts(target_prompts)
            click.echo("Созданы базовые промпты")
            
    except Exception as e:
        click.echo(f"Ошибка при копировании шаблона: {e}")
        # Fallback к базовым промптам
        create_basic_prompts(bot_dir / "prompts")

def copy_from_bot_template(template: str, bot_dir: Path, bot_id: str):
    """Копирует шаблон из существующего бота"""
    try:
        template_dir = PROJECT_ROOT / Path("bots") / template
        if not template_dir.exists():
            raise click.ClickException(f"Шаблон {template} не найден")
        
        # Копируем основной файл бота в корневую директорию
        template_bot_file = PROJECT_ROOT / Path(f"{template}.py")
        if template_bot_file.exists():
            bot_file = PROJECT_ROOT / Path(f"{bot_id}.py")
            shutil.copy2(template_bot_file, bot_file)
            
            # Заменяем название бота в файле
            content = bot_file.read_text(encoding='utf-8')
            content = content.replace(f'BotBuilder("{template}")', f'BotBuilder("{bot_id}")')
            content = content.replace(f'bot_id="{template}"', f'bot_id="{bot_id}"')
            bot_file.write_text(content, encoding='utf-8')
        
        # Копируем .env файл
        template_env = template_dir / ".env"
        if template_env.exists():
            env_file = bot_dir / ".env"
            shutil.copy2(template_env, env_file)
            
            # Заменяем BOT_ID в .env
            env_content = env_file.read_text(encoding='utf-8')
            env_content = env_content.replace(f'BOT_ID={template}', f'BOT_ID={bot_id}')
            env_file.write_text(env_content, encoding='utf-8')
        
        # Копируем промпты
        template_prompts = template_dir / "prompts"
        target_prompts = bot_dir / "prompts"
        
        if template_prompts.exists():
            for prompt_file in template_prompts.glob("*.txt"):
                shutil.copy2(prompt_file, target_prompts / prompt_file.name)
        
        # Копируем тесты
        template_tests = template_dir / "tests"
        target_tests = bot_dir / "tests"
        
        if template_tests.exists():
            for test_file in template_tests.glob("*"):
                if test_file.is_file():
                    shutil.copy2(test_file, target_tests / test_file.name)
        
        click.echo(f"Шаблон скопирован из {template}")
        
    except Exception as e:
        click.echo(f"Ошибка при копировании шаблона {template}: {e}")
        raise

def create_basic_prompts(prompts_dir: Path):
    """Создает базовые промпты"""
    # Системный промпт
    (prompts_dir / "system_prompt.txt").write_text(
        "Ты - помощник. Твоя задача помогать пользователям с их вопросами.\n"
        "Будь дружелюбным и полезным.",
        encoding='utf-8'
    )
    
    # Приветственное сообщение
    (prompts_dir / "welcome_message.txt").write_text(
        "👋 Привет! Я ваш помощник.\n\n"
        "Чем могу помочь?",
        encoding='utf-8'
    )
    
    # Финальные инструкции
    (prompts_dir / "final_instructions.txt").write_text(
        """<instruction>
КРИТИЧЕСКИ ВАЖНО: В НАЧАЛЕ КАЖДОГО своего ответа добавляй служебную информацию в формате:

{
  "этап": id,
  "качество": 1-10,
  "события": [
    {
      "тип": тип события,
      "инфо": детали события
    }
  ],
  "файлы": [],
  "каталоги": []
}

ДОСТУПНЫЕ ОБРАБОТЧИКИ СОБЫТИЙ:
- example_event: Пример обработчика события. Используй для демонстрации.
  Пример: {"тип": "example_event", "инфо": {"data": "пример данных"}}

ДОСТУПНЫЕ ЗАПЛАНИРОВАННЫЕ ЗАДАЧИ:
- example_task: Пример запланированной задачи. Используй для демонстрации.
  Пример: {"тип": "example_task", "инфо": "через 1 час: напомнить о чем-то"}

Используй эти обработчики и задачи, когда это уместно в диалоге.
</instruction>""",
        encoding='utf-8'
    )

if __name__ == "__main__":
    cli()