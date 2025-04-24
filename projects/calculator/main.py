def main():
    while first_num := input("Enter first number or blank to quit: "):
        try:
            first_num = int(first_num)
            second_num = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            match operator:
                case "+":
                    print(f"The result is {first_num+second_num}")
                case "-":
                    print(f"The result is {first_num-second_num}")
                case "*":
                    print(f"The result is {first_num*second_num}")
                case "/":
                    print(f"The result is {first_num/second_num}")
                case _:
                    print("Please enter operator between (+, -, *, /)")
        except ZeroDivisionError:
            print("Zero division error.")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
