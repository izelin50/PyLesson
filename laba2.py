def add(name, surname):
    global f
    f.write("\n"+name + " " + surname)
    f.sort()
def find(surname,optio):

f = open("students.txt", "r+", encoding="utf8")
add("Лось", "Лосев")
f.close()

