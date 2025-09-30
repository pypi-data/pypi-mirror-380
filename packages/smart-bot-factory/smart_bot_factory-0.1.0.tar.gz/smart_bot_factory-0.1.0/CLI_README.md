# Smart Bot Factory CLI

CLI система для управления ботами на основе Smart Bot Factory.

## Установка

```bash
uv pip install -e .
```

## Использование

### Через запускалку (рекомендуется)

```bash
# Показать список ботов
python launcher.py list

# Создать нового бота
python launcher.py create my-bot minimal-bot

# Запустить бота
python launcher.py run my-bot

# Запустить тесты
python launcher.py test my-bot

# Настроить конфигурацию
python launcher.py config my-bot

# Управление промптами
python launcher.py prompts my-bot --list
python launcher.py prompts my-bot --edit system_prompt
python launcher.py prompts my-bot --add new_prompt
```

### Прямо через CLI

```bash
# Показать список ботов
uv run python -m smart_bot_factory.cli list

# Создать нового бота
uv run python -m smart_bot_factory.cli create my-bot minimal-bot

# Запустить бота
uv run python -m smart_bot_factory.cli run my-bot

# Запустить тесты
uv run python -m smart_bot_factory.cli test my-bot
```

## Структура бота

При создании бота создается следующая структура:

```
bots/
└── my-bot/
    ├── my-bot.py              # Основной файл бота
    ├── .env                   # Конфигурация
    ├── prompts/               # Промпты
    │   ├── system_prompt.txt
    │   ├── welcome_message.txt
    │   └── final_instructions.txt
    ├── tests/                 # Тесты
    ├── reports/               # Отчеты
    └── welcome_files/         # Приветственные файлы
```

## Команды

### `list`
Показать список доступных ботов

### `create <bot_id> [template]`
Создать нового бота на основе шаблона

**Шаблоны:**
- `base` (по умолчанию) - базовый шаблон на основе growthmed-october-24
- `<bot_name>` - копия существующего бота из папки bots/

### `run <bot_id>`
Запустить бота

### `test <bot_id>`
Запустить тесты бота

**Опции:**
- `--file <filename>` - запустить тесты только из указанного файла
- `-v, --verbose` - подробный вывод
- `--max-concurrent <number>` - максимальное количество потоков

### `config <bot_id>`
Открыть конфигурацию бота в редакторе

### `prompts <bot_id>`
Управление промптами бота

**Опции:**
- `--list` - показать список промптов
- `--edit <prompt_name>` - редактировать промпт
- `--add <prompt_name>` - добавить новый промпт

## Примеры

### Создание и запуск бота

```bash
# 1. Создать бота (с базовым шаблоном)
uv run sbf create support-bot

# Или создать копию существующего бота
uv run sbf create support-bot2 support-bot

# 2. Настроить конфигурацию
uv run sbf config support-bot

# 3. Запустить бота
uv run sbf run support-bot
```

### Управление промптами

```bash
# Показать список промптов
uv run sbf prompts support-bot --list

# Редактировать системный промпт
uv run sbf prompts support-bot --edit system_prompt

# Добавить новый промпт
uv run sbf prompts support-bot --add help_prompt
```

### Тестирование

```bash
# Запустить все тесты
uv run sbf test support-bot

# Запустить тесты с подробным выводом
uv run sbf test support-bot --verbose

# Запустить тесты из конкретного файла
uv run sbf test support-bot --file test_scenarios.yaml
```

## Требования

- Python 3.9+
- uv (для управления зависимостями)
- Настроенные .env файлы для каждого бота

## Структура проекта

```
chat-bots/
├── launcher.py                    # Запускалка
├── src/smart_bot_factory/         # Библиотека
│   ├── cli.py                     # CLI интерфейс
│   ├── core/                      # Основные компоненты
│   ├── events/                    # Система событий
│   ├── integrations/              # Интеграции
│   └── services/                  # Сервисы
├── bots/                          # Папка с ботами
│   ├── minimal-bot/               # Пример бота
│   └── my-bot/                    # Ваш бот
└── bot_testing.py                 # Система тестирования
```
