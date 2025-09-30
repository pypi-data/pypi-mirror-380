# Smart Bot Factory

Библиотека для создания умных чат-ботов с системой обработчиков событий и планировщиком задач.

## Особенности

- ✅ **Использует существующие файлы** - не создает новые, а расширяет функциональность
- ✅ **Декораторы для обработчиков событий** - простое добавление логики
- ✅ **Планировщик задач** - ИИ может планировать напоминания и задачи
- ✅ **Интеграция с промптами** - автоматически добавляет информацию об обработчиках в промпт
- ✅ **Структура bots/bot-id/** - каждый бот в своей папке

## Установка

```bash
# Установка зависимостей
uv add smart-bot-factory

# Или если используете pip
pip install smart-bot-factory
```

## Быстрый старт

### 1. Создание бота

```python
# bots/my-bot/my-bot.py
import asyncio
from pathlib import Path
import sys

# Добавляем корень проекта в путь
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from smart_bot_factory import BotBuilder, event_handler, schedule_task

# Обработчик события записи на прием
@event_handler("appointment_booking", "Записывает пользователя на прием к врачу")
async def book_appointment(user_id: int, appointment_data: dict):
    # Ваша логика записи в БД
    return {
        "status": "success",
        "appointment_id": f"apt_{user_id}",
        "message": f"Запись создана"
    }

# Задача для планирования напоминаний
@schedule_task("send_reminder", "Отправляет напоминание пользователю")
async def send_reminder(user_id: int, message: str):
    # Логика отправки напоминания
    return {"status": "sent"}

async def main():
    # Создаем и запускаем бота
    bot_builder = BotBuilder("my-bot")
    await bot_builder.build()
    
    # Здесь интеграция с вашим main.py
    # или запуск бота напрямую

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Структура бота

```
bots/my-bot/
├── my-bot.py              # Запускалка бота
├── prompts/               # Промпты
│   ├── final_instructions.txt
│   ├── welcome_message.txt
│   └── help_message.txt
├── tests/                 # Тесты
│   └── scenarios.yaml
├── reports/               # Отчеты по тестам
└── files/                 # Файлы для отправки
    └── brochure.pdf
```

### 3. Промпт с обработчиками

В `prompts/final_instructions.txt` добавьте:

```
После получения телефона в ответе в служебном json добавь в массив "события" 
событие с тип="appointment_booking" и инфо="имя, телефон, выбранный врач/процедура"

Для планирования напоминания добавь событие с тип="send_reminder" 
и инфо="через 2 часа: напомнить о приеме"
```

## Декораторы

### @event_handler

Регистрирует обработчик события:

```python
@event_handler("phone_collection", "Обрабатывает получение номера телефона")
async def handle_phone(user_id: int, phone_data: dict):
    # Логика обработки номера
    return {"status": "processed"}
```

### @schedule_task

Регистрирует задачу для планирования:

```python
@schedule_task("send_reminder", "Отправляет напоминание пользователю")
async def send_reminder(user_id: int, message: str):
    # Логика отправки напоминания
    return {"status": "sent"}
```

## Как работает планировщик

ИИ может планировать задачи, указывая время в поле `инфо`:

```json
{
  "события": [
    {
      "тип": "send_reminder",
      "инфо": "через 2 часа: напомнить о приеме к кардиологу"
    }
  ]
}
```

Поддерживаемые форматы времени:
- "через 2 часа"
- "через 30 минут"
- "через 1 день"
- "через 2 часа 30 минут"

## Интеграция с существующими файлами

Библиотека автоматически интегрируется с вашими файлами:

- `handlers.py` - обработка событий
- `bot_utils.py` - функция `process_events`
- `openai_client.py` - клиент OpenAI
- `supabase_client.py` - клиент Supabase
- `config.py` - конфигурация

## Примеры событий

### Запись на прием
```json
{
  "тип": "appointment_booking",
  "инфо": "Иван Петров, +7-999-123-45-67, кардиолог, завтра 14:00"
}
```

### Сбор номера телефона
```json
{
  "тип": "phone_collection", 
  "инфо": "Мария Сидорова, +7-888-555-44-33, интересуется имплантацией"
}
```

### Планирование напоминания
```json
{
  "тип": "send_reminder",
  "инфо": "через 1 день: напомнить о подготовке к операции"
}
```

## CLI команды

```bash
# Создать нового бота
sbf create my-bot template-bot

# Запустить бота
sbf run my-bot

# Запустить тесты
sbf test my-bot

# Управление промптами
sbf prompts my-bot --list
sbf prompts my-bot --edit final_instructions
```

## Архитектура

```
src/smart_bot_factory/
├── core/
│   └── bot_builder.py      # Строитель ботов
├── events/
│   └── decorators.py       # Декораторы обработчиков
├── integrations/
│   └── __init__.py         # Интеграция с существующими файлами
└── __init__.py
```

## Преимущества

1. **Простота** - добавьте декоратор и готово
2. **Гибкость** - ИИ сам решает когда вызывать обработчики
3. **Интеграция** - использует ваши существующие файлы
4. **Масштабируемость** - легко добавлять новые обработчики
5. **Автоматизация** - планировщик задач работает в фоне

## Лицензия

MIT
