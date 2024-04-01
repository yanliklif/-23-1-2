
r = True
while r == True:
    try:
        a = int(input('Введите число'))
        break
    except:
        print("Вы ввели не число")
while r == True:
    try:
        b = int(input('Введите второе число'))
        break
    except:
        print("Вы ввели не число")
print(f"Вы ввели числа {a} и {b}")
while r == True:
    c = int(input('Введите дейсвие(+(1), -(2), *(3), /(4))'))
    if (c == 1):
        print(f"{a} + {b} = {a + b}")
        break
    elif (c == 2):
        print(f"{a} - {b} = {a - b}")
        break
    elif (c == 3):
        print(f"{a} * {b} = {a * b}")
        break
    elif (c == 4):
        if (b == 0):
            print("На 0 делить нельзя")
            break
        else:
            print(f"{a} / {b} = {a / b}")
            break
    else:
        print("Вы ввели число не от 1 до 4")
