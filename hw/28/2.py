import random


def new_password():
    password = ""
    for i in range(random.randint(7, 10)):
        password += chr(random.randint(33, 126))
    return password


print(new_password())
