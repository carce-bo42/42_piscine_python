from sys import argv as lol

if len(lol) == 1:
    print("No arguments provided")
    exit(0)
    
print(' '.join(str(k[::-1]).swapcase() for k in lol[:0:-1]))