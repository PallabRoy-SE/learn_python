from functools import reduce

l = [2, 5, 455, 2, 2, 1, 5, 7, 8, 3, 23, 6, 34, 6, 34, 21, 6, 7]

sq = map(lambda x: x * x, l)
print(list(sq))

fl = filter(lambda x: x > 5, l)
print(list(fl))

mul = reduce(lambda a, b: a * b, l, 1)
print(mul)
