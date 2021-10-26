import telebot
from telebot import types
import init_book_bot as ini
import book_bot_token as tkn

### Variables

game_start = False
current_chapter_id = None

## Entry point

if  __name__ != "__main__" :
    print("You can't import this module")
    raise SystemExit

bot = telebot.TeleBot(tkn.BOT_TOKEN)

### handlers

@bot.message_handler(commands=[ini.HELP_COMMAND])
def help_comand(message):
	bot.send_message(message.from_user.id, ini.HELP_MESSAGE)

@bot.message_handler(commands=[ini.START_COMMAND])
def start_command(message):
    global game_start
    if not game_start :
        game_start = True
        bot.send_message(message.from_user.id, ini.START_MESSAGE)
    else :
        bot.send_message(message.from_user.id, ini.START_DURING_GAME)

@bot.message_handler(commands=[ini.RESET_COMMAND])
def reset_command(message):
    global game_start
    game_start = False
    current_chapter_id = None
    bot.send_message(message.from_user.id, ini.RESET_MESSAGE)

@bot.message_handler(commands=[ini.ABOUT_COMMAND])
def reset_command(message):
    bot.send_message(message.from_user.id, ini.ABOUT_MESSAGE)
    bot.send_message(message.from_user.id, "Версия: " + ini.VERSION)


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document',
            'text', 'location', 'contact', 'sticker'])
def unknown_command(message):
    bot.send_message(message.from_user.id, ini.UNKNOWN_COMMAND_MESSAGE)


## Блок тестов

import tests 
book =tests.make_simple_book()


### Start book bot

bot.polling(none_stop=True, interval=0)