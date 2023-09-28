
# from my_bot_info import *

import time
import telebot
from telebot.types import Message
the_token="6599230420:AAGos8xN3JtlSSmQOo2BtA3X79qzVrkZ6Cw"

bot=telebot.TeleBot(the_token)
@bot.message_handler(func=lambda m :True)
def rm(m):
    bot.reply_to(m,m.text)
    bot.reply_to(m,"GO GO")
    f = open("demofile2.txt", "w")
    f.write(m.text)
    f.close()
bot.infinity_polling()