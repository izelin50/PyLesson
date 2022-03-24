def add(name, surname):
    f = open("students.txt", "r")
    t = [x for x in f]
    t.append(name + " " + surname)
    t.sort()
    f.close()
    f = open("students.txt", "w")
    for x in t:
        f.write(x + "\n")
    f.close()


def find(surname, name=''):
    if name != '':
        f = open("students.txt", "r")
        s = [a for a in f]
        l = name + " " + surname
        for x in s:
            if l in x:
                print('Yes')
                return True
        f.close()
        print("No")
    else:
        flag = False
        f = open("students.txt", "r")
        s = [a for a in f]
        for x in s:
            if surname in x:
                print(x)
                flag = True
        f.close()
        print("No")
        return flag


def edit(name, surname, new_name="", new_surname=""):
    f = open("students.txt", "r+")
    t = [x for x in f]
    if find(surname, name):
        remove(name, surname)
        add(name, surname)
    else:
        print('No such student')

    f.close()


def remove(surname, name=''):
    try:
        if name != '':
            f = open("students.txt", "r+")
            t = [x for x in f]
            t.remove(name + " " + surname)
            t.sort()
            for x in t:
                f.write(x)
            f.close()
        else:
            if find(surname):
                remove(input('Введите имя и фамилию студента из списка выше'))
    except:
        print("Student not in list")


add("F", "b")
edit("Покемон", "Покемонов", "А", "F")
remove('Лось Лосев')
