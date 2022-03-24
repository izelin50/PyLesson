enter=input().split()
try:
    a=int(enter[1])
    b=int(enter[2])
except:
    print('Некорректный ввод!')
    quit()

if enter[3]=='+':
    print(a+b)
if enter[3]=='-':
    print(a-b)
if enter[3]=='/':
    try:
        print(a/b)
    except:
        print("Ошибка деления на ноль!")

