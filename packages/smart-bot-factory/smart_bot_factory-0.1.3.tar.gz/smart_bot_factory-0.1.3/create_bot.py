#!/usr/bin/env python3
"""
Утилита для создания новых телеграм-ботов на основе существующих шаблонов
Поддерживает автоопределение BOT_ID из имени файла запускалки (v2.1)

Использование:
    python create_bot.py <шаблон> <новый-бот>
    
Примеры:
    python create_bot.py growthmed-october-24 dental-clinic
    python create_bot.py dental-clinic medical-spa
    python create_bot.py growthmed-october-24 my-new-bot
"""

import sys
import shutil
import os
from pathlib import Path


def show_help():
    """Показывает справку по использованию"""
    print("🤖 Создание нового телеграм-бота на основе шаблона")
    print("=" * 55)
    print()
    print("Использование:")
    print("  python create_bot.py <шаблон> <новый-бот>")
    print()
    print("Параметры:")
    print("  шаблон    - имя существующего бота для копирования")
    print("  новый-бот - имя создаваемого бота")
    print()
    print("Примеры:")
    print("  python create_bot.py growthmed-october-24 dental-clinic")
    print("  python create_bot.py dental-clinic medical-spa")
    print("  python create_bot.py growthmed-october-24 my-new-bot")
    print()
    print("🎯 Правила именования ботов:")
    print("  ✅ Можно: латинские буквы, цифры, дефисы")
    print("  ❌ Нельзя: пробелы, кириллица, подчеркивания, спецсимволы")
    print()
    print("Примеры правильных имен:")
    print("  ✅ dental-clinic")
    print("  ✅ medical-spa-2024") 
    print("  ✅ bot1")
    print()
    print("Примеры неправильных имен:")
    print("  ❌ dental clinic (пробелы)")
    print("  ❌ стоматология (кириллица)")
    print("  ❌ dental_clinic (подчеркивания)")
    print("  ❌ dental-clinic! (спецсимволы)")


def validate_bot_name(name: str) -> bool:
    """
    Проверяет корректность имени бота
    
    Args:
        name: имя бота для проверки
        
    Returns:
        True если имя корректно, False иначе
    """
    if not name:
        return False
    
    # Проверяем что содержит только разрешенные символы
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-')
    return all(c in allowed_chars for c in name.lower())


def list_available_bots() -> list:
    """
    Возвращает список доступных ботов-шаблонов
    
    Returns:
        Список имен доступных ботов
    """
    root_dir = Path(__file__).parent
    configs_dir = root_dir / 'configs'
    
    if not configs_dir.exists():
        return []
    
    bots = []
    for bot_dir in configs_dir.iterdir():
        if bot_dir.is_dir():
            # Проверяем что есть соответствующая запускалка
            launcher = root_dir / f'{bot_dir.name}.py'
            if launcher.exists():
                bots.append(bot_dir.name)
    
    return sorted(bots)


def create_new_bot(template_name: str, new_bot_name: str) -> bool:
    """
    Создает новый бот на основе шаблона с поддержкой автоопределения BOT_ID
    
    Args:
        template_name: имя бота-шаблона (например, 'growthmed-october-24')
        new_bot_name: имя нового бота (например, 'dental-clinic')
        
    Returns:
        True если бот создан успешно, False иначе
    """
    root_dir = Path(__file__).parent
    template_config_dir = root_dir / 'configs' / template_name
    new_config_dir = root_dir / 'configs' / new_bot_name
    template_launcher = root_dir / f'{template_name}.py'
    new_launcher = root_dir / f'{new_bot_name}.py'
    
    print(f"🔍 Проверяем шаблон '{template_name}'...")
    
    # Проверяем существование шаблона
    if not template_config_dir.exists():
        print(f"❌ Бот-шаблон '{template_name}' не найден в configs/{template_name}")
        available_bots = list_available_bots()
        if available_bots:
            print(f"📋 Доступные боты-шаблоны: {', '.join(available_bots)}")
        else:
            print("📋 Нет доступных ботов-шаблонов")
        return False
    
    if not template_launcher.exists():
        print(f"❌ Запускалка шаблона '{template_name}.py' не найдена")
        return False
    
    print(f"✅ Шаблон '{template_name}' найден")
    
    # Проверяем валидность имени нового бота
    if not validate_bot_name(new_bot_name):
        print(f"❌ Некорректное имя бота '{new_bot_name}'")
        print("🎯 Имя должно содержать только:")
        print("   - латинские буквы (a-z)")
        print("   - цифры (0-9)")
        print("   - дефисы (-)")
        return False
    
    # Проверяем, что новый бот не существует
    if new_config_dir.exists():
        print(f"❌ Бот '{new_bot_name}' уже существует в configs/{new_bot_name}")
        return False
    
    if new_launcher.exists():
        print(f"❌ Файл '{new_bot_name}.py' уже существует")
        return False
    
    print(f"🎯 Создаем нового бота '{new_bot_name}' на основе '{template_name}'...")
    
    try:
        # Создаем папку конфигурации
        print(f"📁 Создаем папку configs/{new_bot_name}...")
        shutil.copytree(template_config_dir, new_config_dir)
        
        # Создаем запускалку
        print(f"🚀 Создаем запускалку {new_bot_name}.py...")
        shutil.copy2(template_launcher, new_launcher)
        
        # Очищаем .env файл от BOT_ID (поскольку теперь он определяется автоматически)
        env_file = new_config_dir / '.env'
        if env_file.exists():
            print(f"🔧 Обрабатываем файл .env...")
            
            # Читаем .env и удаляем строки с BOT_ID
            env_content = env_file.read_text(encoding='utf-8')
            
            lines = env_content.split('\n')
            cleaned_lines = []
            removed_lines = []
            
            for line in lines:
                # Пропускаем строки с BOT_ID и комментарии о нем
                if (line.startswith('BOT_ID=') or 
                    line.startswith('# Bot Identity') or
                    'bot_id' in line.lower()):
                    removed_lines.append(line.strip())
                    continue
                cleaned_lines.append(line)
            
            # Удаляем лишние пустые строки в начале
            while cleaned_lines and not cleaned_lines[0].strip():
                cleaned_lines.pop(0)
            
            # Записываем обратно
            env_file.write_text('\n'.join(cleaned_lines), encoding='utf-8')
            
            if removed_lines:
                print(f"🗑️ Удалены строки из .env:")
                for line in removed_lines:
                    print(f"   - {line}")
            
            print(f"✅ Файл .env очищен от BOT_ID (теперь определяется автоматически)")
        
        # Проверяем наличие обязательных файлов
        prompts_dir = new_config_dir / 'prompts'
        welcome_file = prompts_dir / 'welcome_message.txt'
        
        if not prompts_dir.exists():
            print(f"⚠️ Папка prompts не найдена, создаем...")
            prompts_dir.mkdir()
        
        if not welcome_file.exists():
            print(f"⚠️ Файл welcome_message.txt не найден, создаем заглушку...")
            welcome_file.write_text(
                f"Добро пожаловать в {new_bot_name}!\n\n"
                "Это автоматически созданное приветственное сообщение.\n"
                "Отредактируйте этот файл для настройки вашего бота.",
                encoding='utf-8'
            )
        
        print(f"✅ Бот '{new_bot_name}' успешно создан!")
        
    except Exception as e:
        print(f"❌ Ошибка при создании бота: {e}")
        
        # Очищаем частично созданные файлы
        if new_config_dir.exists():
            shutil.rmtree(new_config_dir)
        if new_launcher.exists():
            new_launcher.unlink()
            
        return False
    
    # Выводим инструкции по дальнейшей настройке
    print(f"\n📋 Следующие шаги:")
    print(f"1. Отредактируйте configs/{new_bot_name}/.env")
    print(f"   ⚠️  НЕ добавляйте BOT_ID - он определяется автоматически!")
    print(f"2. Настройте промпты в configs/{new_bot_name}/prompts/")
    print(f"   📝 Особенно важен welcome_message.txt")
    print(f"3. Запустите: python {new_bot_name}.py")
    print(f"\n🤖 Bot ID будет автоматически: {new_bot_name}")
    
    # Показываем пример для Docker
    print(f"\n🐳 Для Docker добавьте сервис в docker-compose.yml:")
    print(f"  {new_bot_name}:")
    print(f"    build: .")
    print(f"    command: python {new_bot_name}.py")
    print(f"    volumes:")
    print(f"      - ./configs/{new_bot_name}:/app/configs/{new_bot_name}:ro")
    print(f"    restart: unless-stopped")
    print(f"    container_name: sales-{new_bot_name}")
    
    return True


def main():
    """Главная функция"""
    print("🤖 Утилита создания телеграм-ботов v2.1")
    print("=" * 45)
    print()
    
    # Проверяем аргументы командной строки
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        return
    
    if len(sys.argv) != 3:
        print("❌ Ошибка: требуется 2 аргумента")
        print("💡 Используйте: python create_bot.py <шаблон> <новый-бот>")
        print("💡 Или: python create_bot.py --help для справки")
        return
    
    template_name = sys.argv[1].strip()
    new_bot_name = sys.argv[2].strip()
    
    # Проверяем что аргументы не пустые
    if not template_name or not new_bot_name:
        print("❌ Ошибка: имена ботов не могут быть пустыми")
        return
    
    # Проверяем что боты не одинаковые
    if template_name == new_bot_name:
        print("❌ Ошибка: имя нового бота должно отличаться от шаблона")
        return
    
    print(f"📋 Параметры:")
    print(f"   Шаблон: {template_name}")
    print(f"   Новый бот: {new_bot_name}")
    print()
    
    # Создаем бота
    success = create_new_bot(template_name, new_bot_name)
    
    if success:
        print("\n🎉 Создание завершено успешно!")
        print(f"🚀 Теперь настройте конфигурацию и запустите: python {new_bot_name}.py")
    else:
        print("\n❌ Создание не удалось. Исправьте ошибки и попробуйте снова.")
        sys.exit(1)


if __name__ == "__main__":
    main()