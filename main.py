import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse

load_dotenv()
# def wait(chat_id, question):
#     # bot.create_timer(6, choose, author_id=chat_id, message=question)


# def notify_progress(secs_left):
#     print("Осталось секунд:", secs_left)


# bot = ptbot.Bot(token)
# bot.create_countdown(5, notify_progress)
# bot.send_message(chat_id, notify_progress)


# def choose(author_id, message):
#     bot.send_message(chat_id, 'время вышло!')


# bot.reply_on_message(notify_progress)
# bot = ptbot.Bot(token)
# bot.reply_on_message(wait)
# bot.run_bot()

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)



def notify_progress(secs_left, message_id, message):  
    bot.update_message(chat_id, message_id, "осталось {} секунд \n {}".format(secs_left,render_progressbar(message,message - secs_left)  ))


#Когда боту пишут, он запускает функцию wait. Она ничего никому не пишет, а ставит таймер на 5 секунд.
#Когда таймер пройдёт, запустится функция choose. Она запустится потому что мы передали её в метод bot.create_timer(5, choose).
def wait(chat_id, question):
    time = parse(question)
    message_id = bot.send_message(chat_id,  "Запускаю таймер...")
    bot.create_countdown( time, notify_progress, message_id=message_id, message=time)
    bot.create_timer(time, choose, chat_id=chat_id, message=time) #question=question. Эти аргументы можно переименовать как угодно


def choose(chat_id, message): #отдельный кусочек кода, который можно запустить попозже
    bot.send_message(chat_id, "Время вышло!")


token = os.environ['TOKEN']
bot = ptbot.Bot(token)
chat_id = os.environ['CHAT_ID']
bot.send_message(chat_id, "Бот запущен")
bot.reply_on_message(wait) #здесь функция wait передаётся в метод bot.reply_on_message()
#Метод reply_on_message будет ждать до тех пор, пока боту кто-нибудь не напишет. Как только боту напишет человек, reply_on_message запустит вашу функцию
bot.run_bot() 
