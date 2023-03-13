import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
    exit(1)

if (not sys.argv[1].isnumeric()):
    print("AssertionError: more than one argument are provided")
    exit(1)

n = int(sys.argv[1])
if n == 0:
    print("I'm Zero")
elif n % 2 == 0:
    print("I'm Even")
else :
    print("I'm Odd")
