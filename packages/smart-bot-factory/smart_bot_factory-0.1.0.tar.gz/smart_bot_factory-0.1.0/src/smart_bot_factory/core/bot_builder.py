"""
Строитель ботов для Smart Bot Factory
"""

import os
import sys
import asyncio
import logging
from pathlib import Path
from typing import Optional, Dict, Any, List

from ..integrations import (
    Config, OpenAIClient, SupabaseClient, 
    ConversationManager, AdminManager, PromptLoader
)
from ..events.decorators import get_handlers_for_prompt

logger = logging.getLogger(__name__)

class BotBuilder:
    """
    Строитель ботов, который использует существующие файлы проекта
    и добавляет новые возможности через декораторы
    """
    
    def __init__(self, bot_id: str, config_dir: Optional[Path] = None):
        """
        Инициализация строителя бота
        
        Args:
            bot_id: Идентификатор бота
            config_dir: Путь к директории конфигурации (по умолчанию configs/bot_id)
        """
        self.bot_id = bot_id
        self.config_dir = config_dir or Path("bots") / bot_id
        
        # Компоненты бота
        self.config: Optional[Config] = None
        self.openai_client: Optional[OpenAIClient] = None
        self.supabase_client: Optional[SupabaseClient] = None
        self.conversation_manager: Optional[ConversationManager] = None
        self.admin_manager: Optional[AdminManager] = None
        self.prompt_loader: Optional[PromptLoader] = None
        
        # Флаги инициализации
        self._initialized = False
        
        logger.info(f"🏗️ Создан BotBuilder для бота: {bot_id}")
    
    async def build(self) -> 'BotBuilder':
        """
        Строит и инициализирует все компоненты бота
        
        Returns:
            BotBuilder: Возвращает self для цепочки вызовов
        """
        if self._initialized:
            logger.warning(f"⚠️ Бот {self.bot_id} уже инициализирован")
            return self
        
        try:
            logger.info(f"🚀 Начинаем сборку бота {self.bot_id}")
            
            # 1. Инициализируем конфигурацию
            await self._init_config()
            
            # 2. Инициализируем клиенты
            await self._init_clients()
            
            # 3. Инициализируем менеджеры
            await self._init_managers()
            
            # 4. Обновляем промпты с информацией о доступных инструментах
            await self._update_prompts_with_tools()
            
            self._initialized = True
            logger.info(f"✅ Бот {self.bot_id} успешно собран и готов к работе")
            
            return self
            
        except Exception as e:
            logger.error(f"❌ Ошибка при сборке бота {self.bot_id}: {e}")
            raise
    
    async def _init_config(self):
        """Инициализация конфигурации"""
        logger.info(f"⚙️ Инициализация конфигурации для {self.bot_id}")
        
        # Устанавливаем BOT_ID в переменные окружения
        os.environ['BOT_ID'] = self.bot_id
        
        # Загружаем .env файл если существует
        env_file = self.config_dir / ".env"
        if env_file.exists():
            from dotenv import load_dotenv
            load_dotenv(env_file)
            logger.info(f"📄 Загружен .env файл: {env_file}")
        
        # Проверяем, установлен ли уже путь к промптам в файле запускалки
        if "PROMT_FILES_DIR" in os.environ:
            logger.info(f"📁 Путь к промптам уже установлен: {os.environ['PROMT_FILES_DIR']}")
        else:
            # Устанавливаем правильный путь к промптам ПОСЛЕ загрузки .env
            # Берем значение из .env и добавляем к пути bots/bot-id/
            prompts_subdir = os.environ.get("PROMT_FILES_DIR", "prompts")
            logger.info(f"🔍 PROMT_FILES_DIR из .env: {prompts_subdir}")
            logger.info(f"🔍 config_dir: {self.config_dir}")
            
            prompts_dir = self.config_dir / prompts_subdir
            logger.info(f"🔍 Полный путь к промптам: {prompts_dir}")
            logger.info(f"🔍 Существует ли папка: {prompts_dir.exists()}")
            
            # ВАЖНО: Устанавливаем правильный путь ДО создания Config
            if prompts_dir.exists():
                os.environ["PROMT_FILES_DIR"] = str(prompts_dir)
                logger.info(f"📁 Установлен путь к промптам: {prompts_dir}")
            else:
                logger.error(f"❌ Папка с промптами не найдена: {prompts_dir}")
                # Устанавливаем путь даже если папки нет, чтобы Config не упал
                os.environ["PROMT_FILES_DIR"] = str(prompts_dir)
        
        # Создаем конфигурацию
        logger.info(f"🔍 PROMT_FILES_DIR перед созданием Config: {os.environ.get('PROMT_FILES_DIR')}")
        self.config = Config()
        logger.info(f"✅ Конфигурация инициализирована")
    
    async def _init_clients(self):
        """Инициализация клиентов"""
        logger.info(f"🔌 Инициализация клиентов для {self.bot_id}")
        
        # OpenAI клиент
        self.openai_client = OpenAIClient(
            api_key=self.config.OPENAI_API_KEY,
            model=self.config.OPENAI_MODEL,
            max_tokens=self.config.OPENAI_MAX_TOKENS,
            temperature=self.config.OPENAI_TEMPERATURE
        )
        logger.info(f"✅ OpenAI клиент инициализирован")
        
        # Supabase клиент
        self.supabase_client = SupabaseClient(
            url=self.config.SUPABASE_URL,
            key=self.config.SUPABASE_KEY,
            bot_id=self.bot_id
        )
        await self.supabase_client.initialize()
        logger.info(f"✅ Supabase клиент инициализирован")
    
    async def _init_managers(self):
        """Инициализация менеджеров"""
        logger.info(f"👥 Инициализация менеджеров для {self.bot_id}")
        
        # Admin Manager
        self.admin_manager = AdminManager(self.config, self.supabase_client)
        await self.admin_manager.sync_admins_from_config()
        logger.info(f"✅ Admin Manager инициализирован")
        
        # Conversation Manager
        self.conversation_manager = ConversationManager(self.supabase_client, self.admin_manager)
        logger.info(f"✅ Conversation Manager инициализирован")
        
        # Prompt Loader
        self.prompt_loader = PromptLoader(
            prompts_dir=self.config.PROMT_FILES_DIR,
            prompt_files=self.config.PROMPT_FILES
        )
        await self.prompt_loader.validate_prompts()
        logger.info(f"✅ Prompt Loader инициализирован")
    
    async def _update_prompts_with_tools(self):
        """
        Обновляет промпты информацией о доступных обработчиках событий
        """
        logger.info(f"🔧 Обновление промптов с информацией об обработчиках")
        
        # Получаем информацию о доступных обработчиках
        event_handlers_info = get_handlers_for_prompt()
        
        # Если есть обработчики, добавляем их в системный промпт
        if event_handlers_info:
            # Сохраняем информацию о обработчиках для использования в handlers.py
            self._tools_prompt = event_handlers_info
            
            logger.info(f"✅ Промпты обновлены с информацией об обработчиках")
        else:
            self._tools_prompt = ""
            logger.info(f"ℹ️ Нет зарегистрированных обработчиков")
    
    def get_tools_prompt(self) -> str:
        """Возвращает промпт с информацией об инструментах"""
        return getattr(self, '_tools_prompt', '')
    
    def get_status(self) -> Dict[str, Any]:
        """Возвращает статус бота"""
        return {
            "bot_id": self.bot_id,
            "initialized": self._initialized,
            "config_dir": str(self.config_dir),
            "components": {
                "config": self.config is not None,
                "openai_client": self.openai_client is not None,
                "supabase_client": self.supabase_client is not None,
                "conversation_manager": self.conversation_manager is not None,
                "admin_manager": self.admin_manager is not None,
                "prompt_loader": self.prompt_loader is not None
            },
            "tools": {
                "event_handlers": len(get_handlers_for_prompt().split('\n')) if get_handlers_for_prompt() else 0
            }
        }
    
    async def start(self):
        """
        Запускает бота (аналог main.py)
        """
        if not self._initialized:
            raise RuntimeError(f"Бот {self.bot_id} не инициализирован. Вызовите build() сначала")
        
        logger.info(f"🚀 Запускаем бота {self.bot_id}")
        
        try:
            # Импортируем необходимые компоненты
            from aiogram import Bot, Dispatcher
            from aiogram.fsm.storage.memory import MemoryStorage
            
            # Создаем бота и диспетчер
            bot = Bot(token=self.config.TELEGRAM_BOT_TOKEN)
            storage = MemoryStorage()
            dp = Dispatcher(storage=storage)
            
            # Инициализируем базу данных
            await self.supabase_client.initialize()
            
            # Синхронизируем админов из конфигурации
            await self.admin_manager.sync_admins_from_config()
            
            # Проверяем доступность промптов
            prompts_status = await self.prompt_loader.validate_prompts()
            logger.info(f"Статус промптов: {prompts_status}")
            
            # Устанавливаем глобальные переменные ДО импорта обработчиков
            import sys
            import importlib
            
            # Устанавливаем глобальные переменные в модулях handlers и admin_logic
            try:
                handlers_module = importlib.import_module('handlers')
                handlers_module.config = self.config
                handlers_module.bot = bot
                handlers_module.dp = dp
                handlers_module.supabase_client = self.supabase_client
                handlers_module.openai_client = self.openai_client
                handlers_module.prompt_loader = self.prompt_loader
                handlers_module.admin_manager = self.admin_manager
                handlers_module.conversation_manager = self.conversation_manager
                logger.info("✅ Глобальные переменные установлены в handlers")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось установить глобальные переменные в handlers: {e}")
            
            try:
                admin_logic_module = importlib.import_module('admin_logic')
                admin_logic_module.config = self.config
                admin_logic_module.bot = bot
                admin_logic_module.dp = dp
                admin_logic_module.supabase_client = self.supabase_client
                admin_logic_module.openai_client = self.openai_client
                admin_logic_module.prompt_loader = self.prompt_loader
                admin_logic_module.admin_manager = self.admin_manager
                admin_logic_module.conversation_manager = self.conversation_manager
                logger.info("✅ Глобальные переменные установлены в admin_logic")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось установить глобальные переменные в admin_logic: {e}")
            
            # Также устанавливаем в bot_utils
            try:
                bot_utils_module = importlib.import_module('bot_utils')
                bot_utils_module.config = self.config
                bot_utils_module.bot = bot
                bot_utils_module.dp = dp
                bot_utils_module.supabase_client = self.supabase_client
                bot_utils_module.openai_client = self.openai_client
                bot_utils_module.prompt_loader = self.prompt_loader
                bot_utils_module.admin_manager = self.admin_manager
                bot_utils_module.conversation_manager = self.conversation_manager
                logger.info("✅ Глобальные переменные установлены в bot_utils")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось установить глобальные переменные в bot_utils: {e}")
            
            # Также устанавливаем в debug_routing
            try:
                debug_routing_module = importlib.import_module('debug_routing')
                debug_routing_module.config = self.config
                debug_routing_module.bot = bot
                debug_routing_module.dp = dp
                debug_routing_module.supabase_client = self.supabase_client
                debug_routing_module.openai_client = self.openai_client
                debug_routing_module.prompt_loader = self.prompt_loader
                debug_routing_module.admin_manager = self.admin_manager
                debug_routing_module.conversation_manager = self.conversation_manager
                logger.info("✅ Глобальные переменные установлены в debug_routing")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось установить глобальные переменные в debug_routing: {e}")
            
            # Теперь импортируем и настраиваем обработчики
            from ..integrations import setup_handlers, setup_admin_handlers, setup_utils_handlers
            
            # Настраиваем обработчики запросов
            setup_utils_handlers(dp)    # Утилитарные команды (/status, /help)
            setup_admin_handlers(dp)    # Админские команды (/админ, /стат, /чат)
            setup_handlers(dp)          # Основные пользовательские обработчики
            
            # Логируем информацию о запуске
            logger.info(f"✅ Бот {self.bot_id} запущен и готов к работе!")
            logger.info(f"   📊 Изоляция данных: bot_id = {self.config.BOT_ID}")
            logger.info(f"   👑 Админов настроено: {len(self.config.ADMIN_TELEGRAM_IDS)}")
            logger.info(f"   📝 Загружено промптов: {len(self.config.PROMPT_FILES)}")
            
            # Четкое сообщение о запуске
            print(f"\n🚀 БОТ {self.bot_id.upper()} УСПЕШНО ЗАПУЩЕН!")
            print(f"📱 Telegram Bot ID: {self.config.BOT_ID}")
            print(f"👑 Админов: {len(self.config.ADMIN_TELEGRAM_IDS)}")
            print(f"📝 Промптов: {len(self.config.PROMPT_FILES)}")
            print(f"🔄 Ожидание сообщений...")
            print(f"⏹️  Для остановки нажмите Ctrl+C\n")
            
            # Запуск polling (бесконечная обработка сообщений)
            await dp.start_polling(bot)
            
        except Exception as e:
            logger.error(f"❌ Ошибка при запуске бота {self.bot_id}: {e}")
            import traceback
            logger.error(f"Стек ошибки: {traceback.format_exc()}")
            raise
        finally:
            # Очистка ресурсов при завершении
            if 'bot' in locals():
                await bot.session.close()
