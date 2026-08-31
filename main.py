# from cash_register import *
import random

# cash_register()

max_number = ''

print("     Игра 'Угадай число'    ")

while not (max_number.isdigit() and int(max_number) != 0):
    print("  Введите максимальное число"  )
    max_number = input()

max_number = int(max_number)

rand_number = random.randint(0 ,max_number)

print(rand_number)
