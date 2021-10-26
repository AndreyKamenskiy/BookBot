import telebot
from telebot import types
import init_book_bot as ini
import book_bot_token as tkn
import library as lib

### Variables

game_start = False
current_chapter_id = None
choise = {}

book = None

### Printer methods
def show_chapter(chatID, id = ""):
    if id == "":
        return #TODO: заменить на исключение
    #получить главу
    global book
    if book == None:
        return
    chapter = book.GetChapterById(id)
    if chapter == None:
        return

    global choise
    choise = {}
    text = ""
    count = 0
    keyboard = types.InlineKeyboardMarkup()
    for el in chapter.elements:
        text += el.text
        if el.next != "":
            count += 1
            text += f"<{count}>"
            choise[str(count)] = el.next
            callback_button = types.InlineKeyboardButton(text=str(count), callback_data=str(count))
            keyboard.add(callback_button)
        text += "\n"
    global bot
    if count > 0:
        bot.send_message(chatID, text, reply_markup=keyboard)
    else:
        bot.send_message(chatID, text)

## Entry point

if  __name__ != "__main__" :
    print("You can't import this module")
    raise SystemExit

bot = telebot.TeleBot(tkn.BOT_TOKEN)

### handlers


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global choise
    if call.data in choise.keys:
        show_chapter(call.message.chat.id, choise[call.data])


@bot.message_handler(commands=[ini.HELP_COMMAND])
def help_comand(message):
	bot.send_message(message.from_user.id, ini.HELP_MESSAGE)

@bot.message_handler(commands=[ini.START_COMMAND])
def start_command(message):
    global game_start
    if not game_start :
        game_start = True
        current_chapter_id = "start"
        bot.send_message(message.from_user.id, ini.START_MESSAGE)
        show_chapter(message.from_user.id, current_chapter_id)
    else :
        bot.send_message(message.from_user.id, ini.START_DURING_GAME)

@bot.message_handler(commands=[ini.RESET_COMMAND])
def reset_command(message):
    global game_start
    game_start = False
    global current_chapter_id
    current_chapter_id = ""
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
book = tests.make_simple_book()


### Start book bot

bot.polling(none_stop=True, interval=0)