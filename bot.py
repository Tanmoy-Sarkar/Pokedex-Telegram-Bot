from telegram.ext import *
import config
from pokedex import pokedex
import json
def start_command(update,context):
    username = update.message.chat.first_name
    update.message.reply_text(f"How are you {username}")

def error(update,context):
    print(f"{update} caused error {context.error}")

def message_response(update,context):
    text = str(update.message.text)
    username = update.message.chat.first_name
    if text in ("hi","hello","yo","whats up"):
        response = (f"<b>How are you doing {username}.Enter a pokemon name or id to get info </b>")
    else:
        response = str(pokedex(text))
    update.message.reply_text(response,parse_mode='HTML')

def main():
    updater = Updater(config.api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(MessageHandler(Filters.text,message_response))
    updater.start_polling(3)
    updater.idle()

print("Bot started running")

main()