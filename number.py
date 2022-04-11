import random
lowDigit = 10
highDigit = 50
digit = 0

countInput = 0
win = False
playGame = True
x = 0
startScore = 100
score = 0
maxScore = 0

while (playGame):
    digit = random.randint(lowDigit, highDigit)
    print(f'Загаданное число: {digit}')
    print('-' * 30)
    countInput = 0
    score = startScore
    print('компьютер загадал число, попробуй отгадать!')
    while (not win and score > 0):
        print('-' * 30)
        print(f'Зарабатано очков: {score}')
        print(f'Рекорд: {maxScore}')

        x =""
        while (not x.isdigit()):
            x = input(f'Введите число от {lowDigit} до {highDigit}: ')
            if (not x.isdigit()):
                print('.' * 27 + "Введите, пожалуйста чило. ")
        x = int(x)
        if (x == digit):
            win = True
        else:
            length = abs(x - digit)
            if (length < 3):
                print('Очень горячо!')
            elif (length < 5):
                print('Горячо!')
            elif (length < 10):
                print('Тепло')
            elif (length <15):
                print('Прохладно')
            elif (length < 20):
                print('Холодно')
            else:
                print('Ледяной ветер')
            if (countInput == 7):
                score -= 10
                if (digit % 2 == 0):

