import telebot
bot = telebot.TeleBot('1759601349:AAEQTMs-k0mEbT_RkmlRfwqAHhjHVIG3IlM')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
