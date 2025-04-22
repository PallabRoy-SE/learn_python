from functools import reduce


def marks(*args, **kwargs):
    print(reduce(lambda a, b: a + b, args))
    for item in kwargs:
        print(f"Result of {item} is {kwargs[item]}.")


marks(2, 42, 52, Pallab=100, rahul=34)
