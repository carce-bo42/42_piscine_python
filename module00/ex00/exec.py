from sys import argv as lol

if len(lol) == 1:
    print("No arguments provided")
    exit(0)
    
print(' '.join([str(k) for k in lol[1]]))