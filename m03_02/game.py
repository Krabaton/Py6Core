from random import randint

# Надо угадать число от 0 до n


def game(n):
    count = 0
    goal = randint(0, n)  # получаем случайное целое число от 0 до n
    while True:
        answer = int(input(f"Угадайте задуманное число от 0 до {n}: "))
        count += 1
        if answer > goal:
            print("Ваше число больше задуманного")
        elif answer < goal:
            print("Ваше число меньше задуманного")
        else:
            print(f"Поздравляем! Вы угадали число за {count} шагов")
            break


if __name__ == '__main__':
    game(10)
