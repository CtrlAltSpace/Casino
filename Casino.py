import random
import time

# Choose a random number between 1 and 100
random_number = random.randint(1, 100)

# Ask the player to guess
guess = int(input('Guess a number of 1-100 for a prize of $1,000,000'))

# Check the guess
if guess == random_number:
    print("And, the number is")
    print("...")
    time.sleep(2)
    print(random_number)
    print("Congratulations, here's your $1,000,000")
else:
    print("And, the number is")
    print("...")
    time.sleep(2)
    print(random_number)