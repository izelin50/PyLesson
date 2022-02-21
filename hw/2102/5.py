choise=int(input("1:треугольник\n2:круг\n3:прямоугольник\n"))
data=input("Введите необходимые параметры через пробел").split()
if choise==1:
    a=int(data[0])
    b=int(data[1])
    c=int(data[2])
    p=a+b+c
    print((p*(p-a)*(p-b)*(p-c))**0.5)

elif choise==2:
    print(2*3.14*int(data[0]))
elif choise==3:
    print(int(data[0]*int(data[1])))
else:
    print("Idiot!")