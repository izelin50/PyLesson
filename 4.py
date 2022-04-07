f = open("sber.txt", "r", encoding="utf-8")
dict = {}
f.readline()
for x in f:
    a = x.split(",")

    if a[0] == 'Количество заявок на потребительские кредиты':
        if a[2][:4:] == '2017':
            try:
                dict[a[1]] += int(a[3])
            except:
                dict[a[1]] = int(a[3])
    else: break
del dict['Россия']
print(max(dict, key=dict.get))
f.close()
