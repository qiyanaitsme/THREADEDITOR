import requests
import json
import time
from logger_config import logger
from settings import load_settings
from colorama import Fore, Style

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def load_thread_ids():
    with open('parsedid.json', 'r') as file:
        return json.load(file)['thread_ids']

def manage_threads():
    config = load_config()
    token = config['token']
    settings = load_settings()
    
    if not settings:
        logger.error("Настройки не найдены")
        return

    try:
        thread_ids = load_thread_ids()
        logger.success(f"Загружено {len(thread_ids)} тем")
    except FileNotFoundError:
        logger.error("Файл с темами не найден")
        return

    print(f"\n{Fore.CYAN}Выберите действие:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Открыть темы")
    print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Закрыть темы")
    choice = input(f"{Fore.GREEN}Выберите действие (1/2): {Style.RESET_ALL}")

    is_open = True if choice == "1" else False
    action = "открытия" if is_open else "закрытия"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}"
    }

    for thread_id in thread_ids:
        url = f"https://api.zelenka.guru/threads/{thread_id}?discussion_open={'true' if is_open else 'false'}"
        try:
            response = requests.put(url, headers=headers)
            response.raise_for_status()
            logger.success(f"Тема {thread_id} успешно {'открыта' if is_open else 'закрыта'}")
        except Exception as e:
            logger.error(f"Ошибка при обработке темы {thread_id}")
        
        time.sleep(3)

if __name__ == "__main__":
    manage_threads()
