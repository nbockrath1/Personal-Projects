# Author: Nicholas Bockrath 
# Date: 20221218 
# Description: Play a game of Battleship with the user. 
import random 
grid = ['A','B','C','D','E','F','G','H','I','J']        # Store the board into lists and announce the name of the game to the user 
grid1 = ['1','2','3','4','5','6','7','8','9','10'] 
row = ['O','O','O','O','O','O','O','O','O','O'] 
print("Let's play Battleship!") 
x = grid[random.randrange(10)]                          # Store the randomized coordinates of the battleship in the variables, x and y 
y = grid1[random.randrange(10)] 
print(x,y) 
guess = 0 
answer = None 
while guess < 5:                                        # Until the user makes five wrong attempts or one correct attempt, repeatedly prompt them to guess the coordinates of the battleship 
    print('  ' + ' '.join(grid1))                       # Align the grid1 list properly 
    count = 0 
    while count < 10:                                   # Display the rest of the board 
        print(grid[count] + ' ' + ' '.join(row))        # Print the elements of the grid list horizontally without printing the brackets or commas 
        count += 1 
    answer = input('Enter Your Guess: ')                # Prompt the user for a guess 
    answer = answer.split(' ') 
    if x == answer[0] and y == answer[1]:               # If the user guesses correctly, then let them know and end the game 
        print("You Win!") 
        break 
    else:                                               # If the user does not guess correctly, then let them know if they suck or not and act accordingly 
        guess += 1 
        if guess == 5:                                  # Alert the user if the game is over 
            print('You suck!') 
        if guess == 4:                                  # If the game is not over, then tell the user how many guesses they have left 
            print('Miss! 1 Guess Left.') 
        else: 
            print('Miss! ' + str((5-guess)) + ' Guesses Left.')