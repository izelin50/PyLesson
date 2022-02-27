import random

n = random.randint(1, 10)
while 1:
    t = int(input("Введите число: "))
    if t != n:
        print(">") if t > n else print("<")
    else:
        break
