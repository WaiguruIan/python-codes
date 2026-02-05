#Adm NO: BSCIT-05-0096\2024
#Name: Ian Waiguru

import random  # Import the random module

# Generates a random winning number between 1 and 100
wining_number = random.randint(1, 100)
print("Welcome to the guessing game!")

user_guess = int(input("Enter your guess number between 1 and 100: "))
while user_guess != wining_number:
    if user_guess < wining_number:
        print("Too low! Try again.")
    elif user_guess > wining_number:
            print("Too high! Try again.")
    
    user_guess = int(input("Enter your guess number between 1 and 100: "))

print("Congratulations! You guessed the correct number.")
print("The winning number is: ", wining_number)