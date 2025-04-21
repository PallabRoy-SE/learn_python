def repeat(n):
    def decorator(fn):
        def wrapper(a):
            for i in range(n):
                fn(a)

        return wrapper

    return decorator


@repeat(100)
def say_hello(message):
    print(message)


say_hello("I am repeating...")
