import requests
import json
from logger_config import logger
from settings import load_settings, save_settings

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def get_user_settings():
    settings = load_settings()
    if settings:
        use_saved = input("Использовать сохраненные настройки? (y/n): ").lower()
        if use_saved == 'y':
            logger.success("Загружены сохраненные настройки")
            return settings['forum_id'], settings['user_id']
    
    forum_id = input("Введите ID раздела: ")
    user_id = input("Введите user_id: ")
    save_settings(forum_id, user_id)
    logger.success("Новые настройки сохранены")
    return forum_id, user_id

def parse_threads():
    config = load_config()
    token = config['token']
    forum_id, user_id = get_user_settings()
    
    url = f"https://api.zelenka.guru/threads?forum_id={forum_id}&creator_user_id={user_id}"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        thread_ids = [thread['thread_id'] for thread in data['threads']]
        with open('parsedid.json', 'w') as f:
            json.dump({"thread_ids": thread_ids}, f)
        
        logger.success(f"Успешно получено {len(thread_ids)} тем")

        for thread in data['threads']:
            print("\nthread_id - Айди темы:", thread['thread_id'])
            print("forum_id - раздел:", thread['forum_id'])
            print("thread_title - Название темы:", thread['thread_title'])
            print("=" * 50)
            
    except Exception as e:
        logger.error(f"Ошибка парсинга: {str(e)}")