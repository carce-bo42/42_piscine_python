import random

def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if option is not None \
            and option != "shuffle" and option != "unique" and option != "ordered":
        print("ERROR")
        return 
    
    if type(text) != str:
        print("ERROR")
        return

    lst = text.split(sep)
    if option == "shuffle":
        # Fisher–Yates shuffle Algorithm
        for i in range(len(lst) - 1, 0, -1):
            j = random.randint(0, i)
            lst[i], lst[j] = lst[j], lst[i]
    elif option == "unique":
        lst = list(dict.fromkeys(lst))
    else:
        lst = sorted(lst)

    for l in lst:
        yield l

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)

print()
print()

for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print()
print()

for word in generator(text, sep=" ", option="ordered"):
    print(word)

print()
print()

for word in generator(text, sep=" ", option="unique"):
    print(word)

print()
print()

text = 1.0
for word in generator(text, sep="."):
    print(word)