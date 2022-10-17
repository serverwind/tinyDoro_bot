import telebot
import time

# токен зарегистрированного у @BotFather нового бота
token = 'token'

# создаем бота
bot = telebot.TeleBot(token)

HELP = '''Добро пожаловать в "НАЗВАНИЕ БОТА"!
"Описание техники Помодоро"
Чтобы установить таймер на 25 минут напишите 25.
'''


# вывод справки бота
@bot.message_handler(commands=['help', 'start'])
def help(message):
    bot.send_message(message.chat.id, HELP)


# команда: установить таймер на 25 минут
@bot.message_handler(commands=['add'])
def setTimer(message):
    command = message.text.split(maxsplit=1)
    workMin = command[1]
    bot.send_message(message.chat.id, 'Таймер установлен на ' + workMin + 'минут.')
    workSec = int(workMin)
    regime = 1
    status = True
    while status:
    # по прошествии 25 минут приходит уведомление о том,
    # что нужно сделать перерыв на 5 минут.
    # пользователь жмет ок и уходит на перерыв, таймер стартует.
        if regime == 0:
            regime = 1
            bot.send_message(message.chat.id, 'Время отдохнуть! ' + str(status))
            timer(5, regime)
    # по прошествии 5 минут приходит уведомление, что нужно начать работу
    # пользователь жмет ок, начинает работу, таймер стартует.
        elif regime == 1:
            regime = 0
            bot.send_message(message.chat.id, 'Время поработать! ' + str(status))
            timer(workSec, regime)


# функция работы таймера
def timer(workSec, regime):
    while workSec > 0:
        time.sleep(1)
        workSec -= 1
        print(workSec, 'regime: ', regime)  # для проверки на баги


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Таймер должен быть остановлен.')
    status = False
    print(status)

#цикл запросов на сервер телеграм, чтобы бот проверял отправили ли ему сообщение
bot.polling(none_stop = True)
