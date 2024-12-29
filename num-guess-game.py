import random
import sys
correct_or_error = False
answer = random.randint(1, 101)
try:
    guess = int(input("Enter a number from 1 - 100: "))
except ValueError:
    sys.exit("Please enter a number")
if guess == answer or guess not in range(1, 101):
    correct_or_error = True
    if guess not in range(1, 101):
        sys.exit("Please enter a value from 1 - 100")

try:
    while not correct_or_error:
        guess = int(input("Incorrect! Try again!"))
        if guess == answer or guess not in range(1, 101):
            correct_or_error = True
            if guess not in range(1, 101):
                sys.exit("Please enter a value from 1 - 100")
        
except ValueError:
    sys.exit("Please enter a number")
    

print(f"Correct! THe answer was {answer}")