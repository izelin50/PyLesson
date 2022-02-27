import random


def new_password():
    password = ""
    for i in range(random.randint(7, 10)):
        password += chr(random.randint(33, 126))
    return password


def check_password(password):
    if len(password) >= 8 and not password.islower():
        return True
    return False


counter = 1
while 1:
    s = new_password()
    print(s)
    if check_password(s):
        break
    else:
        counter += 1
print(counter)
