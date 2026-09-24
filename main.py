from cash_register import cash_register
from gan import *

print("  добро пожаловать в игру  ")
print(" 1 - игра \"угадай число\"")
print(" 2 - \"Робот кассир\"")
print(" 0 - выход")
print("  Введите число")
# todo сделать защиту
i = int(input())

if i == 0:
    exit()
elif i == 1:
    gan()
elif i == 2:
    cash_register()