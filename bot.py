import telebot

from telebot import types
import os
from flask import Flask, request

token ="688022098:AAH6XjlozMc-EtBnQboQnhQSoE0xSobGTi0"

bot = telebot.TeleBot(token)

server = Flask(__name__)


@bot.message_handler(commands=['start'])
def otvet(message):
    user_markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='Четная', callback_data='chet')
    b2 = types.InlineKeyboardButton(text='Нечетная', callback_data='nech')
    user_markup.row(b1, b2)
    bot.send_message(message.from_user.id, """Ну привет, ботаны!

Выбирайте нужную неделю)""", reply_markup=user_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'chet':
            user_markup = types.InlineKeyboardMarkup()
            b3 = types.InlineKeyboardButton(text='Понедельник', callback_data='pn')
            b4 = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
            b5 = types.InlineKeyboardButton(text='Среда', callback_data='sr')
            b6 = types.InlineKeyboardButton(text='Четверг', callback_data='cht')
            b7 = types.InlineKeyboardButton(text='Пятница', callback_data='pt')
            b8 = types.InlineKeyboardButton(text='Суббота', callback_data='sb')
            b9 = types.InlineKeyboardButton(text='Назад', callback_data='back')
            user_markup.row(b3, b4)
            user_markup.row(b5, b6)
            user_markup.row(b7, b8)
            user_markup.add(b9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери день)',reply_markup=user_markup)

        elif call.data == 'nech':
            user_markup = types.InlineKeyboardMarkup()
            bb = types.InlineKeyboardButton(text='Понедельник', callback_data='pn1')
            bb1 = types.InlineKeyboardButton(text='Вторник', callback_data='vt1')
            bb2 = types.InlineKeyboardButton(text='Среда', callback_data='sr1')
            bb3 = types.InlineKeyboardButton(text='Четверг', callback_data='cht1')
            bb4 = types.InlineKeyboardButton(text='Пятница', callback_data='pt1')
            bb5 = types.InlineKeyboardButton(text='Суббота', callback_data='sb1')
            bb6 = types.InlineKeyboardButton(text='Назад', callback_data='back')
            user_markup.row(bb, bb1)
            user_markup.row(bb2, bb3)
            user_markup.row(bb4, bb5)
            user_markup.add(bb6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери день)',reply_markup=user_markup)

        elif call.data == 'back':
            user_markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text='Четная', callback_data='chet')
            b2 = types.InlineKeyboardButton(text='Нечетная', callback_data='nech')
            user_markup.row(b1, b2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Выбирайте нужную неделю)', reply_markup=user_markup)




        elif call.data == 'pn':
            user_markup = types.InlineKeyboardMarkup()
            b11 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отдыхай😏', reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'vt':
            user_markup = types.InlineKeyboardMarkup()
            b12 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b12)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Вторник, четная неделя:

8:00 - 9:35 - Экономика - *ЛЕКЦИЯ*. 104/10

9:45 - 11:20 - Правоведение - *ЛЕКЦИЯ*. 107/10

11:30 - 13:05 - Теория химических процессов и органического синтеза - *ЛАБА*. 34/2

13:35 - 15:10 - Теория химических процессов и органического синтеза - *ЛАБА*. 34/2""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'sr':
            user_markup = types.InlineKeyboardMarkup()
            b13 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b13)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Среда, четная неделя:

9:45 - 11:20 - Теория химических процессов и органического синтеза  - *ЛЕКЦИЯ*. 30/2

11:30 - 13:05 - Вычислительная химия - *ЛЕКЦИЯ*. 39/2""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'cht':
            user_markup = types.InlineKeyboardMarkup()
            b14 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b14)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Четверг, четная неделя:

8:00 - 9:35 - Физико-химические свойства растворов - *ЛАБА*. 34/2

9:45 - 11:20 - Физико-химические свойства растворов - *ЛАБА*. 34/2

11:30 - 13:05 - Процессы и аппараты хим. технологии - *Лекция*. 432/1""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'pt':
            user_markup = types.InlineKeyboardMarkup()
            b15 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b15)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Пятница, четная неделя:
            
9:45 - 11:20 - СПК *СЕМИНАР*. 402/10

11:30 - 13:05 - ПиА ХТ *ЛАБА*. 106,108/1 - 2,6,10,14 неделя /// Экология 118/1 - 4,8,12,16 неделя 

13:35 - 15:10 - ПиА ХТ *ЛАБА*. 106,108/1 - 2,6,10,14 неделя /// Экология 118/1 - 4,8,12,16 неделя""",reply_markup=user_markup,parse_mode="Markdown")

        elif call.data == 'sb':
            user_markup = types.InlineKeyboardMarkup()
            b16 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b16)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Суббота, четная неделя:
            
8:00 - 9:35 - Теор. и эксп. методы исследований в технолог. орг. синтеза - *ПРАКТИКА*. 30/2

9:45 - 11:20 - Теор. и эксп. методы исследований в технолог. орг. синтеза - *ПРАКТИКА*. 30/2""",reply_markup=user_markup,parse_mode="Markdown")



        elif call.data == 'back1':
            user_markup = types.InlineKeyboardMarkup()
            b3 = types.InlineKeyboardButton(text='Понедельник', callback_data='pn')
            b4 = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
            b5 = types.InlineKeyboardButton(text='Среда', callback_data='sr')
            b6 = types.InlineKeyboardButton(text='Четверг', callback_data='cht')
            b7 = types.InlineKeyboardButton(text='Пятница', callback_data='pt')
            b8 = types.InlineKeyboardButton(text='Суббота', callback_data='sb')
            b9 = types.InlineKeyboardButton(text='Назад', callback_data='back')
            user_markup.row(b3, b4)
            user_markup.row(b5, b6)
            user_markup.row(b7, b8)
            user_markup.add(b9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери день)',reply_markup=user_markup)


        # НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ НЕЧЕТНАЯ НЕДЕЛЯ

        elif call.data == 'pn1':
            user_markup = types.InlineKeyboardMarkup()
            bс1 = types.InlineKeyboardButton(text='Назад', callback_data='back2')
            user_markup.add(bс1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отдыхай😏', reply_markup=user_markup)

        elif call.data == 'vt1':
            user_markup = types.InlineKeyboardMarkup()
            bс2 = types.InlineKeyboardButton(text='Назад', callback_data='back2')
            user_markup.add(bс2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Вторник, нечетная неделя:

8:00 - 9:35 - ПиАХТ - *ЛЕКЦИЯ*. 432/1

9:45 - 11:20 - СПК - *ПРАКТИКА*. 206/10

11:30 - 13:05 - Экономика - *ПРАКТИКА*. 202/10""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'sr1':
            user_markup = types.InlineKeyboardMarkup()
            bс3 = types.InlineKeyboardButton(text='Назад', callback_data='back2')
            user_markup.add(bс3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Среда, нечетная неделя:

8:00 - 9:35 - ПиАХТ - *ПРАКТИКА*. 116/1

9:45 - 11:20 - Экология - *ПРАКТИКА*. 118/1

11:30 - 13:05 - ВХ в научных и инжереных расчетах - *ЛАБА*. 34/2 - 5,9,13,17 неделя /// Физико-хим. св-ва растворов - *ЛАБА*. 34/2 - 3,7,11,15 неделя""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'cht1':
            user_markup = types.InlineKeyboardMarkup()
            bс4 = types.InlineKeyboardButton(text='Назад', callback_data='back2')
            user_markup.add(bс4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Четверг, нечетная неделя:

8:00 - 9:35 - СПК - *ЛЕКЦИЯ*. 39/2

9:45 - 11:20 - Экология - *ЛЕКЦИЯ*. 30/2

11:30 - 13:05 - Теория химических процессов органического синтеза - *ЛЕКЦИЯ*. 30/2""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'pt1':
            user_markup = types.InlineKeyboardMarkup()
            bс5 = types.InlineKeyboardButton(text='Назад', callback_data='back2')
            user_markup.add(bс5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""

8:00 - 9:35 - Теория химических процессов органического синтеза *ЛАБА* 34/2

9:45 - 11:20 - Теория химических процессов органического синтеза *ЛАБА* 34/2""", reply_markup=user_markup, parse_mode="Markdown")

        elif call.data == 'sb1':
            user_markup = types.InlineKeyboardMarkup()
            bс6 = types.InlineKeyboardButton(text='Назад', callback_data='back2')
            user_markup.add(bс6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отдыхай😏',reply_markup=user_markup)



        elif call.data == 'back2':
            user_markup = types.InlineKeyboardMarkup()
            bb = types.InlineKeyboardButton(text='Понедельник', callback_data='pn1')
            bb1 = types.InlineKeyboardButton(text='Вторник', callback_data='vt1')
            bb2 = types.InlineKeyboardButton(text='Среда', callback_data='sr1')
            bb3 = types.InlineKeyboardButton(text='Четверг', callback_data='cht1')
            bb4 = types.InlineKeyboardButton(text='Пятница', callback_data='pt1')
            bb5 = types.InlineKeyboardButton(text='Суббота', callback_data='sb1')
            bb6 = types.InlineKeyboardButton(text='Назад', callback_data='back')
            user_markup.row(bb, bb1)
            user_markup.row(bb2, bb3)
            user_markup.row(bb4, bb5)
            user_markup.add(bb6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери день)',reply_markup=user_markup)

        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Это невозможно')


@bot.message_handler(commands=['help'])
def wer(message):
    bot.send_message(message.from_user.id, """Спокойно ☝🏻

Я все порешаю 👌🏻👌🏻👌🏻

Жми /start""")


@bot.message_handler(content_types=['text'])
def f(message):
    if message.text == '🛢':
        bot.send_message(message.from_user.id, """💵💵💵

Жми /start""")
    else:
        bot.send_message(message.from_user.id, 'Не понимаю) Лучше жми /start')


@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://bot3xtf2.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))