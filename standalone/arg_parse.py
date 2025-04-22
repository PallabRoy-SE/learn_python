import argparse

parser = argparse.ArgumentParser(description="Simple calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operator", choices=["add", "sub", "mul", "div"], help="Operator")

args = parser.parse_args()

print(args)

match (args.operator):
    case "add":
        print(f"The result is: ", args.num1 + args.num2)
    case "sub":
        print(f"The result is: ", args.num1 - args.num2)
    case "mul":
        print(f"The result is: ", args.num1 * args.num2)
    case "div":
        print(f"The result is: ", args.num1 / args.num2)
    case _:
        print("Please provide proper operator 'add', 'sub', 'mul' or 'div'")
