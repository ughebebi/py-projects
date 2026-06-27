from make import *

height = 0
cost = 0

print("\t Здравствуйте!")
print(" Сколько пришло человек?")
people = int(input())
# todo сделать проверку.
for  i in range(1,people+1):
    print("Введите рост",i,"человека.")
    height = int(input())
    cost += ticket(height)

print("с вас итого:",cost,"рублей")