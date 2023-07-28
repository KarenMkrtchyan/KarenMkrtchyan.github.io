import sys

try:
    x = int(input("x: "))
    y=int(input("y: "))
except ValueError:
    print("dumbass")
    sys.exit(1)

try:
    print(x/y)
except ZeroDivisionError:
    print("dumbass")
    sys.exit(1)