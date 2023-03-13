import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
    exit(1)

if (not sys.argv[1].isnumeric()):
    print("AssertionError: argument is not an integer")
    exit(1)

print(("I'm Even", "I'm Zero", "I'm Odd")[(((int(sys.argv[1]) % 2) * 2) - 1) + 1])