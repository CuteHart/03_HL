# Check for an integer with optional upper/lower
# limits and an optional exit code for infinite mode
# /quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    # Set up error messages

    # If any integer is allowed ...
    if low is None and high is None:
        error = "Please enter an integer"

    # If the number needs to be more than an
    # integer (i.e. rounds/'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f" more than/equal to {low}")

    # If the number needs to be between low and high
    else:
        error = (f"Please enter an integer that is"
                 f" between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # Check for infinite mode/exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low
            if low is not None and response < low:
                print(error)

            # Check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # If response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Guessing loop

# Replace number below with random number between high/low values
secret = 7

# Parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# Set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # Ask the user to guess the number
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # Check that they don't want to quit
    if guess == "xxx":
        # Set end game to use so that outer loop can be broken
        end_game = "yes"
        break

    # Check that guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses")
        continue

    # If guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    # Add one to the number of guesses used
    guesses_used += 1

    # Compare the user's guess with the secret number

    # If we have guesses left ...
    if guess < secret and guesses_used < guesses_allowed:
        feedback = ("Too low, please try a higher number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = ("Too high, please try a lower number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")

    # When the secret number is guessed, we have three different
    # feedback options (lucky/'phew'/well done)
    elif guess == secret:

        if guesses_used == 1:
            feedback = "🍀 Lucky! You got it on the first guess. 🍀🍀"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

    # Print feedback to user
    print(feedback)
