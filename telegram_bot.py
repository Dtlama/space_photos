from dotenv import load_dotenv
from time import sleep
import telegram
import random
import os


if __name__ == '__main__':
    load_dotenv()
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    delay = os.getenv('DELAY', '14400')
    bot = telegram.Bot(token=tg_bot_token)
    filesindir = os.listdir('images')
    while True:
        file_name = random.choice(filesindir)
        file_path = os.path.join('images', file_name)
        with open(file_path, 'rb') as file:
            bot.send_photo(chat_id=tg_chat_id, photo=file)
        sleep(int(delay))
