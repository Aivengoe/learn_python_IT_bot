from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import tele_token, PROXY
import logging
import random


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def emoji():
    emojis_list = ['😁','😉','😋','😒','😏','😜','😨','😱']
    emoji = random.choice(emojis_list)
    return(emoji)

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(f"{text} {emoji()}")

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: {}, Chat Id: {}, Message: {}".format(update.message.chat.username,
                update.message.chat.id, update.message.text[:10]))
    update.message.reply_text(f"{user_text} {emoji()}")

def main():
    mybot = Updater(tele_token, request_kwargs=PROXY)

    logging.info('Bot is launched')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()