import ptbot
from dotenv import load_dotenv
import os
from pytimeparse import parse


load_dotenv()
CHAT_ID = os.environ['CHAT_ID']
TOKEN = os.environ['TOKEN']
BOT = ptbot.Bot(TOKEN)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id, message):  
    BOT.update_message(CHAT_ID, message_id, "осталось {} секунд \n {}".format(secs_left,render_progressbar(message,message - secs_left)  ))


def wait(CHAT_ID, question):
    time = parse(question)
    message_id = BOT.send_message(CHAT_ID,  "Запускаю таймер...")
    BOT.create_countdown( time, notify_progress, message_id=message_id, message=time)
    BOT.create_timer(time, choose, CHAT_ID=CHAT_ID, message=time) 


def choose(CHAT_ID, message): 
    BOT.send_message(CHAT_ID, "Время вышло!")


def main():
    BOT.send_message(CHAT_ID, "Бот запущен")
    BOT.reply_on_message(wait)
    BOT.run_bot()
    

if __name__ == '__main__':
    main()