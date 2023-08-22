# Code made by https://github.com/EduContin

import logging
import telegram
import json

from datetime import datetime, timedelta
from telegram.ext import CommandHandler, Updater

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Set up bot and group IDs
TOKEN = '6492737948:AAFOTDjxkx7e0lhvHf7JMBz-EjcIQstn1tA'
group_id = -1001986931762

OWNER_ID = 1001986931762
DATA_FILE = 'schedule.json'  # Path to JSON that stores all data about memberships
CODES_FILE = 'codes.txt'  # Path to TXT that stores all codes to be redeemed

bot = telegram.Bot(TOKEN)

# On /start replies with welcome msg
def start(update, context):
    user_id = update.effective_user.id
    chat_info = bot.get_chat(chat_id=user_id)
    username = chat_info.username

    bot.send_message(chat_id=user_id,
                     text=f"WELCOME!\nThat's the /start reply message.",
                     parse_mode="HTML")

# Reads data from JSON
def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

# ... (other functions remain unchanged)

def main():
    # Set up dispatcher and job queue
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', start))
    dp.add_handler(CommandHandler('redeem', redeem))

    # Load scheduled removal jobs
    load_jobs()

    # Start the bot
    updater.start_polling()
    logging.info("Bot started")
    updater.idle()

if __name__ == '__main__':
    main()

# Code made by https://github.com/EduContin
