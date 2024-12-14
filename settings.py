import json
import os
from logger_config import logger

def load_settings():
    if os.path.exists('settings.json'):
        try:
            with open('settings.json', 'r') as file:
                return json.load(file)
        except Exception as e:
            logger.error("Ошибка загрузки настроек")
    return None

def save_settings(forum_id, user_id):
    settings = {
        "forum_id": forum_id,
        "user_id": user_id
    }
    try:
        with open('settings.json', 'w') as file:
            json.dump(settings, file)
        logger.success("Настройки сохранены")
    except Exception as e:
        logger.error("Ошибка сохранения настроек")