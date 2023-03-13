import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
    exit(1)

if not sys.argv[2].isnumeric():
    print("AssertionError: more than one argument are provided")
    exit(1)
# text = sys.argv[1].translate(str.maketrans('', '', string.punctuation)) erases punctuation from string XD
# text = (sys.argv[1].translate(str.maketrans('', '', string.punctuation))).split() splits in spaces
print([word for word in (sys.argv[1].translate(str.maketrans('', '', string.punctuation))).split() if len(word) > int(sys.argv[2])])