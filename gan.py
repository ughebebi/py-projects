import random

def gan():

    att = 0
    max_number = ''
    inputed_number = ""



    print("     Игра 'Угадай число'    ")
    while not (max_number.isdigit() and int(max_number) != 0):
        print("  Введите максимальное число"  )
        max_number = input()
    max_number = int(max_number)
    rand_number = random.randint(0 ,max_number)
    while inputed_number != rand_number:
        att = att + 1
        inputed_number = ""
        print("Угадайте число.")
        while not (inputed_number.isdigit() and int(inputed_number) != 0):
            inputed_number = input()
        inputed_number = int(inputed_number)
        if inputed_number == rand_number :
            print("Угадали")
            print(att)
            print('попыток')
        elif inputed_number < rand_number:
            print("Больше")
        elif inputed_number > rand_number:
            print("Меньше")