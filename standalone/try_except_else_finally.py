def div(a, b):
    try:
        c = a / b
        print(c)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("No error occurred.")
    finally:
        print("Cleaning...")


try:
    div(int(input("Enter a number: ")), int(input("Enter another number: ")))
except Exception as e:
    print(e)
