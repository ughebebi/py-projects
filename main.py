from make import *

height = 0
cost = 0

print("\t Здравствуйте!")
print(" Сколько пришло человек?")
# people = int(input())
people = input()
if people.isdigit() and int(people) != 0:
    print("число")
else:
    print("не число")
people = int(people)
# todo сделать проверку роста.
for  i in range(1,people+1):
    print("Введите рост",i,"человека.")
    height = int(input())
    cost += ticket(height)

print("с вас итого:",cost,"рублей")