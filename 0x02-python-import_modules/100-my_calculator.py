#!/usr/bin/python3
import sys
import calculator_1 as calc

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, op, b = sys.argv[1:]
    a = int(a)
    b = int(b)
    result = None

    if op == '+':
        result = calc.add(a, b)
    elif op == '-':
        result = calc.sub(a, b)
    elif op == '*':
        result = calc.mul(a, b)
    elif op == '/':
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, result))
