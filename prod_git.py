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
    regime = 1
    command = message.text.split(maxsplit=1)
    workMin = command[1]
    bot.send_message(message.chat.id, 'Таймер установлен на ' + workMin + ' минут.')
    workTimer(message, workMin, regime)


# процесс переключения режимов таймера с работы на отдых
def workTimer(message, workMin, regime):
    workSec = int(workMin)

    if regime == 0:
        bot.send_message(message.chat.id, 'Время отдохнуть! Введите "yaw" чтобы начать.')

        @bot.message_handler(commands=['yaw'])
        def startRest(message):
            regime = 1
            timer(5, workMin, regime, message)
    elif regime == 1:
        bot.send_message(message.chat.id, 'Время поработать! Введите "yes" чтобы начать.')

        @bot.message_handler(commands=['yes'])
        def startWork(message):
            regime = 0
            timer(workSec, workMin, regime, message)


# функция работы таймера
def timer(workSec, workMin, regime, message):
    while workSec > 0:
        time.sleep(1)
        workSec -= 1
    workTimer(message, workMin, regime)


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Таймер должен быть остановлен.')


# цикл запросов на сервер телеграм, чтобы бот
# проверял отправили ли ему сообщение
bot.polling(none_stop=True)
