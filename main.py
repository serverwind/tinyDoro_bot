import time

HELP = '''Добро пожаловать в "НАЗВАНИЕ БОТА"!
"Описание техники Помодоро"
Чтобы установить таймер на 25 минут напишите 25.
'''

# команда: установить таймер на 25 минут
def setTimer():
    workMin = int(input('Чтобы установить таймер на 25 минут напишите "25": '))
    workSec = workMin
    regime = 1
    return workSec, regime

workSec, regime = setTimer() # сохраняем значения из этой ф-ии, чтобы их можно было использовать в других ф-ях.

# функция работы таймера
def timer(workSec, regime):
    while workSec > 0:
        time.sleep(1)
        workSec -= 1
        print(workSec, 'regime: ', regime)

# основной цикл программы и старт таймера
def startTimer(workSec, regime):
    while True:
    # по прошествии 25 минут приходит уведомление о том, что нужно сделать перерыв на 5 минут
    # пользователь жмет ок и уходит на перерыв, таймер стартует.
        if regime == 0:
            regime = 1
            userInput = input('Время отдохнуть! Напишите что-нибудь если готовы: ')
            timer(5, regime)
    # по прошествии 5 минут приходит уведомление, что нужно начать работу
    # пользователь жмет ок, начинает работу, таймер стартует.
        elif regime == 1:
            regime = 0
            userInput = input('Время поработать! Напишите что-нибудь если готовы: ')
            timer(workSec, regime)

startTimer(workSec, regime)
