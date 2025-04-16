import ptbot
from dotenv import load_dotenv
import os
from pytimeparse import parse





def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(chat_id, secs_left, message_id, message):  
    bot.update_message(chat_id, message_id, "осталось {} секунд \n {}".format(secs_left,render_progressbar(message,message - secs_left)  ))


def wait(chat_id, question):
    time = parse(question)
    message_id = bot.send_message(chat_id,  "Запускаю таймер...")
    bot.create_countdown( time, notify_progress, message_id=message_id, message=time)
    bot.create_timer(time, choose, chat_id=chat_id, message=time) 


def choose(message, chat_id): 
    bot.send_message(chat_id, "Время вышло!")


def main():
    chat_id = os.environ['CHAT_ID']
    bot.send_message(chat_id, "Бот запущен")
    bot.reply_on_message(wait)
    bot.run_bot()
    

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TOKEN']
    bot = ptbot.Bot(token)
    main()