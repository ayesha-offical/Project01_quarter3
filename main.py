import random

print("This is a number guessing game 😊 /n you got 5 attempt to guess the number 50 and 100 , let's Start the game 😍")
number_guess_range = random.randrange(50, 100)
chances = 5

guess_conter = 0

while guess_conter<chances:

    guess_conter += 1
    user_guess = int(input("Please Enter your guess: "))
    if user_guess == number_guess_range:
        print(f"The number is {number_guess_range} and you find it right!👏🏻🎉 in the {guess_conter} attempt")
        break
    elif guess_conter >= chances  and user_guess != number_guess_range:
        print(f"Sorry😞 you have lost the game, the number was {number_guess_range}")

    elif user_guess < number_guess_range:
        print("The number is Low than your guess, Try Again")

    elif user_guess > number_guess_range:
        print("The number is High than your guess, Try Again")

