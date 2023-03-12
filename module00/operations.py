import sys

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 3 10")
    exit(0)
elif not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    print("Non numeric arguments detected")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(f'{"Sum:":12} {a + b}')
    print(f'{"Difference:":12} {a - b}')
    print(f'{"Product:":12} {a * b}')

    if (b != 0):
        float_str = str(a / b)
        # [::-1] traverses the string in reverse
        num_decimal_places = float_str[::-1].find('.')
        if num_decimal_places > 4:
            # [:-k] means print the string without the last k characters,
            # [:-k + 4] allows to print the string omitting all characters
            #           from the end except all exceeding the forth decimal place,
            print(f'{"Quotient:":12} {float_str[:-num_decimal_places + 4] + "..."}')
        else:
            print(f'{"Quocient:":12} {float_str}')
        print(f'{"Remainder:":12} {a % b}')
    else:
        print(f'{"Quocient:":12} {"ERROR (division by zero)"}')
        print(f'{"Remainder:":12} {"ERROR (modulo by zero)"}')

