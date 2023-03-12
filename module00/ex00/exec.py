from sys import argv as lol

if len(lol) == 1:
    print("No arguments provided")
    exit(0)

concatenation = lol[1]
for a in lol[2:]:
    concatenation += " " + a

print(concatenation)