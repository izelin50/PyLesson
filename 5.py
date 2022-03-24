import random

import requests

a = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt").content
while True:
    input('Ваш вопрос: ')
    print(random.choice(a))
