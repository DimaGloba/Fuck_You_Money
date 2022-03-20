import telebot
from telebot import types


token = '5172672324:AAGHvS9IEQkSxJezlChTtB5st0sWgsF85Xs'

bot = telebot.TeleBot(token)

user_name = None
user_monthly_income = None  # доход
user_monthly_expense = None  # расход


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот по улучшению твоей жизни давай знакомиться. Как тебя зовут?')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global user_name, user_age, user_monthly_expense, user_monthly_income
    if message.text == "Меня не зовут, я сам прихожу":
        bot.send_message(message.chat.id, 'Чё умный самый, пшёл вон отсюда')
    else:
        bot.send_message(message.chat.id, 'Приятно познакомиться, ' + message.text + '. Если ты тоже заитересован в улучшении своей жизни предлагаю ответить на несколько вопросов. Сколько тебе лет?')
        user_name = message.text
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('Менее 20000р')
        item2 = types.KeyboardButton('20000 - 35000р')
        item3 = types.KeyboardButton('35000 - 50000р')
        item4 = types.KeyboardButton('Более 50000р')
        markup.add(item1)
    #if
    #    bot.send_message(message.chat.id, 'Сколько в месяц ты зарабатываешь. Не переживай все данные будут в безопастномти.')
    #    user_age = int(message.text)




bot.polling()