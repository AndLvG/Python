import sys

try:
    if len(sys.argv) == 3:
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        num1, num2 = int(num1), int(num2)
        if round(num1) == num1 and round(num2) == num2:
            print(num1 + num2)
        else:
            print(0)
    else:
        print(0)
except ValueError:
    print(0)
