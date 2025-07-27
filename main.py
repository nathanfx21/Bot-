import logging
import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    update.message.reply_text('Welcome to Nathan FX Signal Bot! 🚀')

def post_signal(update, context):
    signal = ' '.join(context.args)
    if signal:
        context.bot.send_message(chat_id=CHANNEL_ID, text=f'📈 *NEW SIGNAL*
{signal}', parse_mode='Markdown')
        update.message.reply_text('Signal sent!')
    else:
        update.message.reply_text('Please provide a signal to post.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signal", post_signal))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()