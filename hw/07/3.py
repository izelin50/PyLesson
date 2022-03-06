data = [1, 5, 6.3, 6, None, 2.0, -4, None]
i, s = 0
for x in data:
    if x is None:
        continue
    i += 1
    s += x
s /= i
for i in range(len(data)):
    if data[i] is None:
        data[i] = s
