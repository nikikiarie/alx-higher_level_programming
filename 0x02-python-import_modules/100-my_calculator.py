#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])

    if operator == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif operator == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    elif operator == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    else:
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
