import random

def random_number(x):
    number = random.randint(1,x)
    user_guess = 0
    print("----Lets play a game.----")
    while user_guess != number:
       user_guess = int(input(f"Guess a number between 1 and {x}: "))
       if user_guess > number:
           print("Sorry guess again. Too high.")
       elif user_guess < number:
           print("Sorry guess again. Too low.")
    
    print(f"Congratulations! You guessed the correct number {number}.")


random_number(10)
