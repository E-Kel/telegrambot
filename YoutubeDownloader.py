import telebot
import time


bot_token = '{paste here token of your new bot}'
bot = telebot.TeleBot(token=bot_token)


def find_number(message):
    video_id = None

    if 'youtube.com/' in message:

            video_id = message[message.find('watch?v=')+8:]
    if 'youtu.be/' in message:
            video_id = message[message.find('youtu.be/')+9:]
    return video_id

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"youtube downloader")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Send me a link with video')

@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
    texts = message.text.split()
    video_id = find_number(texts[0])
    if len(video_id) == 11:
        bot.reply_to(message, 'www.ssyoutube.com/watch?v={}'.format(video_id))
    else:
        bot.reply_to(message, 'invalid link/ try again')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
