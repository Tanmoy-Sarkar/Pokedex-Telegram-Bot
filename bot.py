from telegram.ext import *
import config

def start_command(update,context):
    username = update.message.chat.first_name
    update.message.reply_text(f"How are you {username}")
def error(update,context):
    print(f"{update} caused error {context.error}")

def main():
    updater = Updater(config.api_key,use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    updater.start_polling()
    updater.idle()

print("Bot started running")

main()