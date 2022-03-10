documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def start(enter):
    if enter == "p":
        print(name_by_number(input('Введите номер: ')))
    elif enter == "s":
        print(place_by_number(input("Введите номер: ")))
    elif enter == "/":
        print(get_all())
    elif enter == "q":
        quit(0)
    elif enter == "ads":
        print(new_dir(input("Введите номер новой полки ")))
    elif enter == "ds":
        print(del_dir(input("Введите номер удаляемой полки ")))
    elif enter == "ad":
        print(new_doc())
    elif enter == "d":
        print(del_doc(input('Введите номер удаляемого документа ')))
    elif enter == "m":
        print(move_doc(input('Введите номер перемещаего документа '), input('Введите номер полки ')))
    else:
        print("Команда не найдена")

def move_doc(n, m):
    try:
        directories[m].append(n)
        directories[place_by_number(n)].remove(n)
    except:
        return "Полки не существует"
    return 'Если существовала полка и документ, он перемещен на эту полку'


def del_doc(n):
    for i in range(len(documents)):
        if documents[i]["number"] == n:
            documents.pop(i)
            return "Документ удален"
    return "Документ не найден"


def new_doc():
    documents.append({"type": input('type'), "number": input('number'), "owner": input('owner')})
    directories[input('dir')] = documents[len(documents) - 1]["number"]


def del_dir(n):
    if not directories[n]:
        directories.pop(n)
        return "Полка удалена"
    return "Полка не может быть удалена: она не пустая!"


def new_dir(n):
    directories[n] = []
    return "Новая полка успешно добавлена"


def name_by_number(n):
    for doc in documents:
        if doc['number'] == n:
            return doc['name']


def place_by_number(n):
    for dir in directories.keys():
        if n in directories[dir]:
            return dir


def get_all():
    for doc in documents:
        print((key, doc[key]) for key in doc.keys())


while 1:
    try:
        start(input("Введите название команды: "))
    except:
        print("Что-то сломалось... Попробуйте ещё раз :)")