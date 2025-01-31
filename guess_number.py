from random import randint
number = randint(1,100)
print('Угадайте число от 1 до 100')
count = 0

while True:
    guess = int(input('Введите число: '))
    if guess < number :
        print('Ваше число меньше того, что загадано.')
    
    elif guess > number :
        print('Ваше число больше того, что загадано.')

    elif guess == number :
        break
    count += 1
    

print('Отличная интуиция! Вы угадали число :0')
print(f'У вас ушло на это {count} попыток.')