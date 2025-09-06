import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 7   # you can change the number of attempts
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            return
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print(f"\n❌ Sorry! You've used all {max_attempts} attempts.")
    print(f"The correct number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
