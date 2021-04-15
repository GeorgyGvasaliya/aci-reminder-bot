from config import token, chat_id, designers_url, qa_url, DESIGN_EARLY, DESIGN_LATE, QA_EARLY, QA_LATE
import telebot
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def cancel_repeater(message):
    if message.text.lower() == 'ok' and DESIGN_EARLY <= datetime.today().strftime('%H:%M') < DESIGN_LATE:
        bot.send_message(message.chat.id, 'Ok, repeating message will not send. See you next day(s)')
        scheduler.remove_job('des_repeater')
    elif message.text.lower() == 'ok' and QA_EARLY <= datetime.today().strftime('%H:%M') < QA_LATE:
        bot.send_message(message.chat.id, 'Ok, repeating message will not send. See you next day(s)')
        scheduler.remove_job('qa_repeater')


@bot.message_handler(commands=['start', 'help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Hi, this bot will remind you about QA and designers meetings.\n' +
                     'Message will send 15 and 5 minutes before.\n' + 'You can cancel second message - just write "ok".')


def designers_message_reminder():
    bot.send_message(chat_id, "Do not forget about meeting with designers " + designers_url)
    scheduler.add_job(designers_message_repeater, 'cron', day_of_week='fri', hour=14, minute=55, id='des_repeater')


def designers_message_repeater():
    bot.send_message(chat_id, "5 minutes left " + designers_url)
    scheduler.remove_job('des_repeater')


def qa_message_reminder():
    bot.send_message(chat_id, "Do not forget about QA MT sync " + qa_url)
    scheduler.add_job(qa_message_repeater, 'cron', day_of_week='mon-fri', hour=11, minute=55, id='qa_repeater')


def qa_message_repeater():
    bot.send_message(chat_id, "5 minutes left " + qa_url)
    scheduler.remove_job('qa_repeater')


scheduler = BackgroundScheduler()
scheduler.add_job(qa_message_reminder, 'cron', day_of_week='mon-fri', hour=11, minute=45, id='qa')
scheduler.add_job(designers_message_reminder, 'cron', day_of_week='fri', hour=14, minute=45, id='design')
scheduler.start()

if __name__ == '__main__':
    bot.polling()
