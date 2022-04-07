import json

def add():
    task = {}
    task["category"] = input("Category: ")
    task["name"] = input("Name: ")
    task["time"] = input("Time: ")
    todo.append(task)
def show():
    for task in todo:
        print(task)
def exit():
    with open('todo.json',"w") as f:
        json.dump(todo, f)
    print("Tasks saved")
    quit()

with open('todo.json') as f:
    todo = json.load(f)


while 1:
    c = int(input("Укажите число:"))
    if c==1: add()
    elif c==2: show()
    elif c==3: exit()

