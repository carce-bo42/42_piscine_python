import random

n = random.randint(1, 99)

print("This is an interactive guessing game!\n" \
       + "You have to enter a number between 1 and 99 to find out the secret number.\n" \
       + "Type 'exit' to end the game.\n" \
       + "Good luck!")

attempts = 0
print(f"NUMBER IS {n}")

while True:
    try:
        attempts += 1
        guess = input("What's your guess between 1 and 99?")
        guess = int(guess)
        if guess == n:
            print(f"You won in {attempts} attempts!")
            break
        else:
            print("Too high!") if [guess > n] else print("Too low!")
    except ValueError:
        if guess == "exit":
            print("Goodbye!")
            break
        print("That's not a number")
    except:
        print("Unknown error")