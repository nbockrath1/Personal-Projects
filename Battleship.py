# Author: Nicholas Bockrath 
# Date: 20221218 
# Description: Play a game of Battleship with the user. 
import random 
grid = ['A','B','C','D','E','F','G','H','I','J']        # Store the board into lists and announce the name of the game to the user 
grid1 = ['1','2','3','4','5','6','7','8','9','10'] 
rowA = ['O','O','O','O','O','O','O','O','O','O'] 
rowB = ['O','O','O','O','O','O','O','O','O','O'] 
rowC = ['O','O','O','O','O','O','O','O','O','O'] 
rowD = ['O','O','O','O','O','O','O','O','O','O'] 
rowE = ['O','O','O','O','O','O','O','O','O','O'] 
rowF = ['O','O','O','O','O','O','O','O','O','O'] 
rowG = ['O','O','O','O','O','O','O','O','O','O'] 
rowH = ['O','O','O','O','O','O','O','O','O','O'] 
rowI = ['O','O','O','O','O','O','O','O','O','O'] 
rowJ = ['O','O','O','O','O','O','O','O','O','O'] 
print("Let's play Battleship!\n")                       # Announce the name of the game 
while True:                                             # Prompt the user for their battleship's coordinates and check for errors 
    battleship = input("Enter Your Battleship's Coordinates: ")       # Store the battleship's coordinates into the battleship variable 
    if ' ' not in battleship:                                         # Ensure that there is a space between the coordinates by printing 'Error' and repeating loop if there is not 
        print('\nError') 
        continue 
    battleship = battleship.split(' ')                                # Ensure that the first coordinate is a letter and the second is a number by printing 'Error' and repeating loop if they are not 
    try: 
        test = str(battleship[0]) 
        test1 = int(battleship[1]) 
    except: 
        print('\nError') 
        continue 
    break                                                             # Allow the loop to break out of itself if entered coordinates check out 
if battleship[0] == 'A':                                 # Mark the user's battleship's location on the board with the letter 'B' 
    rowA[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'B': 
    rowB[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'C': 
    rowC[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'D': 
    rowD[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'E': 
    rowE[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'F': 
    rowF[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'G': 
    rowG[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'H': 
    rowH[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'I': 
    rowI[int(battleship[1]) - 1] = 'B' 
elif battleship[0] == 'J': 
    rowJ[int(battleship[1]) - 1] = 'B' 
x = grid[random.randrange(10)]                          # Store the randomized coordinates of the battleship in the variables, x and y 
y = grid1[random.randrange(10)] 
answer = [' ', ' '] 
while True:                                             # Until the user makes five wrong attempts or one correct attempt, repeatedly prompt them to guess the coordinates of the battleship 
    if answer[0] == 'A':                                # If the user makes a guess and misses, then mark the spot that they guessed 
        rowA[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'B': 
        rowB[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'C': 
        rowC[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'D': 
        rowD[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'E': 
        rowE[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'F': 
        rowF[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'G': 
        rowG[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'H': 
        rowH[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'I': 
        rowI[int(answer[1]) - 1] = 'X' 
    elif answer[0] == 'J': 
        rowJ[int(answer[1]) - 1] = 'X' 
    print('  ' + ' '.join(grid1))                       # Align the grid1 list properly 
    print(grid[0] + ' ' + ' '.join(rowA))               # Print the rest of the grid 
    print(grid[1] + ' ' + ' '.join(rowB)) 
    print(grid[2] + ' ' + ' '.join(rowC)) 
    print(grid[3] + ' ' + ' '.join(rowD)) 
    print(grid[4] + ' ' + ' '.join(rowE)) 
    print(grid[5] + ' ' + ' '.join(rowF)) 
    print(grid[6] + ' ' + ' '.join(rowG)) 
    print(grid[7] + ' ' + ' '.join(rowH)) 
    print(grid[8] + ' ' + ' '.join(rowI)) 
    print(grid[9] + ' ' + ' '.join(rowJ)) 
    answer = input('\nEnter Your Guess: ')              # Prompt the user for a guess 
    if ' ' not in answer:                               # If the user's guess isn't valid, then restart the loop without taking away a guess 
        print('\nError') 
        continue 
    answer = answer.split(' ') 
    try:                                                # If the first coordinate entered isn't a letter or the second coordinate isn't a number, then print 'Error' and restart the loop 
        test = str(answer[0]) 
        test1 = int(answer[1]) 
    except: 
        print('\nError') 
        continue 
    if x == answer[0] and y == answer[1]:              # If the user guesses correctly, then let them know and end the game 
        print("You Win!") 
        break 
    else:                                              # If the user does not guess correctly, then alert them of their inaccuracy 
        print('Miss!\n') 
    robot_guess_x = random.randrange(10)               # Enter the enemy's guess into variables, robot_guess_x and robot_guess_y 
    robot_guess_y = random.randrange(10) 
    print("\nAI's Guess: " + str(grid[robot_guess_x]) + ' ' + str(robot_guess_y + 1))       # Print the enemy's guess for the user to see 
    if grid[robot_guess_x] == battleship[0] and robot_guess_y == battleship[1]:             # If the enemy guesses the location of the user's battleship accurately, then alert the user of such and end the game 
        print('Your Battleship Has Been Sunk!\nYou Lose!') 
        break 