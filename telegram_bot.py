from dotenv import load_dotenv
import telegram
import os


if __name__ == '__main__':
    load_dotenv()
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=tg_bot_token)
    bot.send_message(chat_id=tg_chat_id, text="I'm gayming")
    print(bot.get_me())
