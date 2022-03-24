import requests
import matplotlib.pyplot as p

a = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat")
a = [int(x) for x in a.content]
print(max(a),min(a),sum(a)/len(a))
p.plot(a)



