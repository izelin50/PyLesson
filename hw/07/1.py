import math


def my_log(data):
    for i in range(len(data)):
        data[i] = None if data[i] <= 0 else math.log2(data[i])
    return data
