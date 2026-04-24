import telebot
bot = telebot.TeleBot('8691470503:AAEwP3VuXU0TgX2tp5CWRFrh85mx6hArhz4')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi my dear husband')


bot.polling(ndone_stop=True)