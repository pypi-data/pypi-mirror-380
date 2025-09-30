#!/usr/bin/env python3
"""
Запускалка для Smart Bot Factory
Простой способ запуска ботов через CLI
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Основная функция запускалки"""
    if len(sys.argv) < 2:
        print("❌ Использование: python launcher.py <команда> [аргументы]")
        print("💡 Примеры:")
        print("  python launcher.py list")
        print("  python launcher.py create my-bot minimal-bot")
        print("  python launcher.py run my-bot")
        print("  python launcher.py test my-bot")
        sys.exit(1)
    
    # Формируем команду для CLI
    cmd = ["uv", "run", "python", "-m", "smart_bot_factory.cli"] + sys.argv[1:]
    
    try:
        # Запускаем команду
        result = subprocess.run(cmd, check=False)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n⏹️ Операция прервана пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
