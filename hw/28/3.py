def check_password(password):
    if len(password) >= 8 and not password.islower():
        return True
    return False
