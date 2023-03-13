import string
from pathlib import Path
import sys
import os

def text_analyzer(text):

    if text == None or len(text) == 0:
        text = input()
    upcase = sum(1 for c in text if c.isupper())
    lowcase = sum(1 for c in text if c.islower())
    punct_marks = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    print(f'- {upcase} upper letter(s)')
    print(f'- {lowcase} lower letter(s)')
    print(f'- {punct_marks} punctuation mark(s)')
    print(f'- {spaces} space(s)')

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("You must provide one argument only")
        exit(0)
    elif len(sys.argv) == 1:
        text_analyzer(None)
    else:
        # if there is one argument, check if it is a file. If some string
        # accidentally coincides with a file name, the file is preferred
        if os.path.exists(sys.argv[1]):
            text = Path(sys.argv[1]).read_text()
            text_analyzer(text)
        else:
            text_analyzer(sys.argv[1])