from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import wikipedia as wiki

# Bot Token is given by BotFather on Telegram while creating bot.
TOKEN = "719781449:AAFPwK2uOz_OEWQCOFVaSAtLMUGphwUCVuk"
updater = Updater(TOKEN)


def get_wiki(word):
    language_list = ["java", "js", "c#", "c++", ""]
    try:
        if word in language_list:
            return "Python is better!"
        elif word == "python":
            return "Best language ever!"
        else:
            return wiki.summary(word)
    except:
        return "Not Found"


def text_pro(bot, update):
    msg = update.message.text.lower()
    sender_name = update.message.from_user.first_name
    chat_id = update.message.chat.id
    print("{}: {}".format(sender_name, msg))
    if msg.startswith('wiki'):
        bot.send_message(chat_id=chat_id, text=get_wiki(msg[5:]))
        print("Bot: Wikipedia summery of {}".format(msg[5:]))
    else:
        bot.send_message(chat_id=chat_id, text="Invalid command")
        print("Bot: Invalid command")


updater.dispatcher.add_handler(MessageHandler(Filters.text, text_pro))
updater.start_polling()
print("server running...")
updater.idle()
