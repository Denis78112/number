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
                    print('Число четное')
                else:
                    print('Число не четное')
            elif (countInput == 6):
                score -= 8
                if (digit % 3 ==0):
                    print('Число делится на 3')
                else:
                    print('Число не делится на 3')
            elif (countInput == 5):
                score -= 4
                if (digit % 4 == 0):
                    print('Число делится на 4')
                else:
                    print('Число не делится на 4')
            elif (countInput > 2 and countInput < 5):
                score -= 2
                if (x > digit):
                    print('Загаданное число меньше вашего')
                else:
                    print('Загаданное число меньше вашего')
            score -= 5
            countInput += 1
        print('*' * 40)
        if (x == digit):
            print('Победа! Поздравляю!')
        else:
            print('Ой, у вас закончались очки. Вы проиграли')

        if (input("Enter - сыграть еще, 0 - выход") == 0):
            playGame = False
        else:
            win = False
        if (score > maxScore):
            maxScore = score
print('*' * 40)
print("""Спасибо за игру""")



