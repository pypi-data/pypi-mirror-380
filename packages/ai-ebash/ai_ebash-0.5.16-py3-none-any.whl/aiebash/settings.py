import yaml
from pathlib import Path
import os
import shutil
from typing import Dict, Any, Optional
from platformdirs import user_config_dir
from aiebash.logger import log_execution_time
import time


# --- Пути к конфигурации ---
APP_NAME = "ai-ebash"
# Путь к конфигу пользователя (e.g., %APPDATA%\ai-ebash\config.yaml)
USER_CONFIG_DIR = Path(user_config_dir(APP_NAME))
USER_CONFIG_PATH = USER_CONFIG_DIR / "config.yaml"
# Путь к дефолтному конфигу
DEFAULT_CONFIG_PATH = Path(__file__).parent / "default_config.yaml"

class Settings:
    """Класс для работы с настройками приложения"""
    def __init__(self):
        self.config_data = {}
        self.load_settings()

    @log_execution_time
    def load_settings(self) -> None:
        """Загружает настройки из файла или создает файл с настройками по умолчанию"""

        # Если файл настроек пользователя не существует
        if not USER_CONFIG_PATH.exists():

            # Создаем директорию, если ее нет
            USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

            # Проверяем наличие файла дефолтного конфига
            if DEFAULT_CONFIG_PATH.exists():
                shutil.copy(DEFAULT_CONFIG_PATH, USER_CONFIG_PATH)
            else:
                return

        # Загружаем настройки из файла
        try:
            with open(USER_CONFIG_PATH, 'r', encoding='utf-8') as f:
                self.config_data = yaml.safe_load(f)
        except Exception:
            self.config_data = {}

    @log_execution_time
    def save_settings(self) -> None:
        """Сохраняет настройки в файл"""
        try:
            # Создаем директорию, если ее нет
            USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

            with open(USER_CONFIG_PATH, 'w', encoding='utf-8') as f:
                yaml.safe_dump(self.config_data, f, indent=2, allow_unicode=True, default_flow_style=False)
        except Exception:
            pass

    @log_execution_time
    def get_value(self, section: str, key: str, default: Any = None) -> Any:
        """Получает значение из настроек"""
        try:
            if section == "global":
                value = self.config_data.get("global", {}).get(key.lower(), default)
                return value
            elif section == "logging":
                value = self.config_data.get("logging", {}).get(key.lower(), default)
                return value
            else:
                # Ищем в supported_LLMs
                value = self.config_data.get("supported_LLMs", {}).get(section, {}).get(key.lower(), default)
                return value
        except Exception:
            return default

    @log_execution_time
    def set_value(self, section: str, key: str, value: Any) -> None:
        """Устанавливает значение в настройках"""
        try:
            if section == "global":
                if "global" not in self.config_data:
                    self.config_data["global"] = {}
                self.config_data["global"][key.lower()] = value
            elif section == "logging":
                if "logging" not in self.config_data:
                    self.config_data["logging"] = {}
                self.config_data["logging"][key.lower()] = value
            else:
                # Сохраняем в supported_LLMs
                if "supported_LLMs" not in self.config_data:
                    self.config_data["supported_LLMs"] = {}
                if section not in self.config_data["supported_LLMs"]:
                    self.config_data["supported_LLMs"][section] = {}
                self.config_data["supported_LLMs"][section][key.lower()] = value

            self.save_settings()
        except Exception:
            pass

    @log_execution_time
    def get_current_llm_name(self) -> str:
        """Возвращает имя текущего LLM"""
        current_llm = self.get_value("global", "current_LLM", "openai_over_proxy")
        return current_llm

    @log_execution_time
    def get_current_llm_config(self) -> Dict[str, Any]:
        """Возвращает конфигурацию текущего LLM"""
        current_llm_name = self.get_current_llm_name()
        config = self.config_data.get("supported_LLMs", {}).get(current_llm_name, {})
        return config

    @log_execution_time
    def get_available_llms(self) -> list:
        """Возвращает список доступных LLM"""
        llms = list(self.config_data.get("supported_LLMs", {}).keys())
        return llms
    
    @log_execution_time
    def get_logging_config(self) -> Dict[str, Any]:
        """
        Возвращает настройки логирования из конфигурации.
        
        Returns:
            Dict[str, Any]: Настройки логирования
        """
        return self.config_data.get("logging", {})


# Создаем глобальный экземпляр настроек
settings = Settings()
