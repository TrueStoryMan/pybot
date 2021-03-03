import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Хто мене створив? つ ◕_◕ ༽つ \
""")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=["sticker"])
def repeat_all_stickers(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()

if __name__ == '__main__':
     bot.infinity_polling()
