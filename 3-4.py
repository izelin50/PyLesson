import requests

f = open("moby_clean.txt", "w")
a = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt").content.split()
a = [str(x)[2:-1].lower().replace(",", '').replace(".", '').replace("--", '') for x in a]

for x in a:
    f.write(x + "\n")
s = {x: a.count(x) for x in a}
s = sorted(s.items(), key=lambda y: y[1], reverse=True)
print(s[0:5],s[-5:])

