from make import *

people = "0"
cost = 0

print("\t Здравствуйте!")

while not (people.isdigit() and int(people) != 0):
    print(" Сколько пришло человек?")
    people = input()

people = int(people)
# todo сделать проверку роста.

for  i in range(1,people+1):
   height = "0"
   while not (height.isdigit() and int(height) != 0 and int(height) <= 235 and int(height) >=90):
        print("Введите рост",i,"человека.")
        height = input()

   height = int(height)
   cost += ticket(height)





print("с вас итого:",cost,"рублей")