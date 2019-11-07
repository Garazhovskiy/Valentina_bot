import telebot, re
import hello2 #import main


bot = telebot.TeleBot('998785258:AAErkmT9Zec0YqJM6RFTwn7vLeRRMPAjHEA')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Привет, я бот который подсчитает твою зарплату
Для продолжения введите через запятую (,)
1) Сколько часов вы будете работать в день?:
2) Сколько вы будете зарабатывать в час?(сумма):
3) Сколько дней в месяц будешь работать?:'''

                     )

@bot.message_handler(content_types=['text'])
def send_text(message):
    data = message.text
    wordlist = re.sub("[^\w]", " ", data).split()
    time_work_day = wordlist[0]
    amount_of_payment = wordlist[1]
    how_many_working = wordlist[2]
    bot.send_message(message.chat.id, hello2.main(time_work_day, amount_of_payment, how_many_working))





























    #bot.send_message(message.chat.id, message.text)





    #if message.text.lower() == 'привет':
    #    bot.send_message(message.chat.id, message.text)
    #elif message.text.lower() == 'пока':
    #    bot.send_message(message.chat.id, 'Прощай, создатель')
    #    send_text2(message)
    #elif message.text.lower() == 'ку':
    #    bot.send_message(message.chat.id, 'кукусики')
    #elif message.text.lower() == 'му':
    #    bot.send_message(message.chat.id, 'мумусики')

bot.polling()