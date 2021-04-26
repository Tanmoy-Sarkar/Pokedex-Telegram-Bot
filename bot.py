from telegram.ext import *
import config_file
from pokedex import pokedex
import json
def start_command(update,context):
    username = update.message.chat.first_name
    update.message.reply_text(f"How are you {username}.Welcome to the pokemon world.Enter a valid pokemon name or ID (upto 890) to get started")

def error(update,context):
    print(f"{update} caused error {context.error}")

def help_command(update,context):
    
    update.message.reply_text("Please Enter a valid pokemon name or ID (upto 890) to get info")

def message_response(update,context):

    text = str(update.message.text).lower()
    username = update.message.chat.first_name
    print(username)
    if text in ("hi","hello","yo","whats up"):
        response = (f"<b>How are you doing {username}.Enter a pokemon name or id to get info </b>")
    else:
        response,photo_url = pokedex(text)
        if response != None and photo_url != None:
            chat_id = update.message.chat_id
            context.bot.send_photo(chat_id=chat_id,photo=photo_url)
        else:
            response = "Sorry didn't understand you. Please Enter a <b>valid</b> pokemon name or <b>ID (upto 890)</b> to get info"


    
    
    update.message.reply_text(response,parse_mode='HTML')

def main():
    updater = Updater(config_file.api_key,use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,message_response))
    dp.add_error_handler(error)
    updater.start_polling(3)
    updater.idle()

print("Bot started running")

main()