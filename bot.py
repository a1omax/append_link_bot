import telebot
import os

FILENAME = "config.txt"

if not os.path.exists(FILENAME):
    while True:
        tkn = input("Введите токен бота:\n")
        try:
            telebot.TeleBot(tkn, "MarkdownV2")
            with open(FILENAME, "w", encoding="utf8") as f:
                f.write(tkn)
            break
        except:
            print("Error")


with open(FILENAME, "r", encoding="utf8") as f:
    TOKEN = f.read()

bot = telebot.TeleBot(TOKEN, "MarkdownV2")

LINK_URL = "https://t.me/tipoviymedic"
LINK_TEXT = "Типовий медик"
ADD_TEXT = f"\n\n[{LINK_TEXT}]({LINK_URL})"


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="Привет, отправь мне ТЕКСТ и я добавлю ссылку в конец")


@bot.message_handler(content_types=["text", "audio", "voice", "video", "photo", "animation"])
def post(message):
    text = message.text or message.caption or ""
    bot.send_message(chat_id=message.chat.id, text=text+ADD_TEXT)





bot.polling(none_stop=True)