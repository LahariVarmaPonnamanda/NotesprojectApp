import random  # used to generate random numbers

print("Welcome to the Number Guessing Game!")

# Step 1: Generate a random number between 1 and 10
secret_num = random.randint(1, 10)  

# from getpass import getpass  
# secret_number = int (getpass("player 1,enter the secret numbet(hidden):"))
    
# Step 2: Initialize variables
guess = 0
attempts = 0

# Step 3: Start the loop
while guess != secret_num:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess < secret_num:
            print("Too low! Try again.")
        elif guess > secret_num:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")



        