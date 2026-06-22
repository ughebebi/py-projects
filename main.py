from make import *

price = 0
price2 = 0

print("\t Здравствуйте!")
print(" Введите рост первого человека")

height = int(input())
price = ticket(height)

print("Введите рост второго человека")
height2 = int(input())
price2 = ticket(height2)

cost = price2 + price

print("с вас итого:",cost,"рублей")