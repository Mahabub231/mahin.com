import random
number = random.randint(1, 100)
attempts = 0
while attempts < 5:
    guess = int(input("Guess the number (1-100): "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
    attempts += 1
else:
    print(f"Sorry, you're out of attempts. The number was {number}.")
