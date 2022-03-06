import random
import statistics

data = [random.randint(1,10) for _ in range(10)]
i = data.index(min(data))
a = data.index(max(data))
if i < a:
    print(sum(data[i:a]) / a - i)
else:
    data[i] = data[a] = statistics.median(data[a:i])
