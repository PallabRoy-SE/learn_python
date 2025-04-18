lucky_num = int(input("Enter your lucky number: "))

match(lucky_num):
    case 1:
        print("Congratulations!! You have won an Iphone.")
    case 4:
        print("Congratulations!! You have won a Macbook.")
    case 7:
        print("Congratulations!! You have won a Mercedes.")
    case _:
        print("Better luck next time!")