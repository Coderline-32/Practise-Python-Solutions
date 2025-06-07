import random


a = [random.randint(1, 100) for _ in range(100)]
b = [random.randint(1, 100) for _ in range(90)]

c = set(a)
d = set(b)
e = c.intersection(d)
print(e)