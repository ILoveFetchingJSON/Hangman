This python project is a number guessing game, where you have to enter a number from 1 - 100. This project imports "random" and "sys".
I set a correct_or_error variable, for if there was an error, i would set it to **True**. I assigned the variable to be false first.
I set a guess variable, which will input the user for a number between 0-100, and convert the value to an integer. Incase the user didn't enter a number, i used error handling.
I set an answer statement, which uses random.choice() to set a random choice. The answer uses the range() function, to set the number from 1 - 100 (101 as an exclusive).
I created an if statement for if the guess was equal to the answer or the guess was out of range (1 - 100). The correct_or_error statement would be set True if the statement was True.
In the if statement, i put another one for if the guess was out of the range. If the statement was True, then we would use sys.exit() to exit the program and let the user know that they must enter a number from 1 - 100.
I made a while loop that gets executed while correct_or_error was not true. WHen the while loop is executed, the guess will keep being user input saying: "Incorrect! Try Again!". I also applied the same settings from the first guess.
When the user has escaped the loops, they will get a message saying "Correct! The answer was" and then the answer.
