import requests
a=requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt").content
l=0
d=0
s=0
for x in a:
    l+=str(x).isdigit()
    d += str(x).isdigit()
    s += str(x)==" "