students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася": 4, "Петя": 9, "Марина": 8, "Люба": 4, "Коля": 5, "Ваня": 10}
good=[];bad = []

for x in students:
    try:
        grade = grades[x]
    except:
        print("Контрольную работу не писал")
    if grade > 7:
        good.append(grade)
    else:
        bad.append(grade)
print(good)
print(bad)
