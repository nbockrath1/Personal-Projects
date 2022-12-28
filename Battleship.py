# Author: Nicholas Bockrath 
# Date: 20221228 
# Description: Create a game of Battleship with the user 
import random 
grid = ['A','B','C','D','E','F','G','H','I','J']        # Store the user's board and the opponent's board into lists and announce the name of the game to the user 
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
rowA1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowB1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowC1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowD1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowE1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowF1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowG1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowH1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowI1 = ['O','O','O','O','O','O','O','O','O','O'] 
rowJ1 = ['O','O','O','O','O','O','O','O','O','O'] 
print("Let's play Battleship!\n") 
def display_board():                                                                      # Create a function, display_board, that will display both boards 
    print('    Player Board\t\t    AI Board')                                                      # Label each board 
    print('  ' + ' '.join(grid1) + '\t\t' + '  ' + ' '.join(grid1))                                # Align the grid1 list properly 
    print(grid[0] + ' ' + ' '.join(rowA) + '\t\t' + grid[0] + ' ' + ' '.join(rowA1))               # Print the rest of the grid 
    print(grid[1] + ' ' + ' '.join(rowB) + '\t\t' + grid[1] + ' ' + ' '.join(rowB1)) 
    print(grid[2] + ' ' + ' '.join(rowC) + '\t\t' + grid[2] + ' ' + ' '.join(rowC1)) 
    print(grid[3] + ' ' + ' '.join(rowD) + '\t\t' + grid[3] + ' ' + ' '.join(rowD1)) 
    print(grid[4] + ' ' + ' '.join(rowE) + '\t\t' + grid[4] + ' ' + ' '.join(rowE1))
    print(grid[5] + ' ' + ' '.join(rowF) + '\t\t' + grid[5] + ' ' + ' '.join(rowF1)) 
    print(grid[6] + ' ' + ' '.join(rowG) + '\t\t' + grid[6] + ' ' + ' '.join(rowG1)) 
    print(grid[7] + ' ' + ' '.join(rowH) + '\t\t' + grid[7] + ' ' + ' '.join(rowH1)) 
    print(grid[8] + ' ' + ' '.join(rowI) + '\t\t' + grid[8] + ' ' + ' '.join(rowI1)) 
    print(grid[9] + ' ' + ' '.join(rowJ) + '\t\t' + grid[9] + ' ' + ' '.join(rowJ1)) 
def pick_battleship():                                                                    # Create a function that prompts the user for their battleship's location 
    while True:                                                           # Prompt the user for their battleship's coordinates and check for errors 
        print('\n') 
        battleship = input("Enter Your Battleship's Coordinates: ")       # Store the battleship's coordinates into the battleship variable 
        print('\n') 
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
        break                                                             # Allow the loop to break out of itself and continue the game if entered coordinates check out 
    if battleship[0] == 'A':                                              # Mark the user's battleship's location on the board with the letter 'B' 
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
    return battleship 
x = grid[random.randrange(10)]                                                           # Store the randomized coordinates of the battleship in the variables, x and y 
y = grid1[random.randrange(10)] 
def play_game():                                                                         # Create a function that operates the game of Battleship 
    answer = [' ', ' '] 
    while True:                                             # Until the location of a battleship is found, repeatedly prompt the user to guess the location of the opponent's battleship and then have the opponent make their randomized guess 
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
        display_board() 
        answer = input('\nEnter Your Guess: ')              # Prompt the user for a guess 
        if ' ' not in answer:                               # If the user's guess isn't valid, then restart the loop and let them repeat their turn 
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
        else:                                              # If the user does not guess correctly, then alert them of their inaccuracy and continue with the opponent's turn 
            while True: 
                robot_guess_x = random.randrange(10)                                                              # Enter the enemy's guess into variables, robot_guess_x and robot_guess_y 
                robot_guess_y = random.randrange(10) 
                if robot_guess_x == 0 and rowA1[int(grid1[robot_guess_y]) - 1] == 'X':                            # If the opponent misses, then mark the guessed coordinates on the opponent's 
                    continue 
                elif robot_guess_x == 1 and rowB1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 2 and rowC1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 3 and rowD1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 4 and rowE1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 5 and rowF1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 6 and rowG1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 7 and rowH1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 8 and rowI1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                elif robot_guess_x == 9 and rowJ1[int(grid1[robot_guess_y]) - 1] == 'X': 
                    continue 
                else: 
                    break 
            print("\n\nMiss!\t\t\t\tAI's Guess: " + str(grid[robot_guess_x]) + ' ' + str(robot_guess_y + 1))      # Alert the user of their inaccuracy and then announce the opponent's guessed coordinates 
        if grid[robot_guess_x] == battleship[0] and (robot_guess_y + 1) == battleship[1]:             # If the enemy guesses the location of the user's battleship accurately, then alert the user of such, mark the location on the opponent's board, and end the game 
            if grid[robot_guess_x] == 'A': 
                rowA1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'B': 
                rowB1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'C': 
                rowC1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'D': 
                rowD1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'E': 
                rowE1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'F': 
                rowF1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'G': 
                rowG1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'H': 
                rowH1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'I': 
                rowI1[int(grid1[robot_guess_y]) - 1] = '!' 
            elif grid[robot_guess_x] == 'J': 
                rowJ1[int(grid1[robot_guess_y]) - 1] = '!' 
            display_board() 
            print('Your Battleship Has Been Sunk!\nYou Lose!') 
            break 
        else:                                                                                         # If the opponent misses, then mark the guessed coordinates on the opponent's board 
            if grid[robot_guess_x] == 'A': 
                rowA1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'B': 
                rowB1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'C': 
                rowC1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'D': 
                rowD1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'E': 
                rowE1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'F': 
                rowF1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'G': 
                rowG1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'H': 
                rowH1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'I': 
                rowI1[int(grid1[robot_guess_y]) - 1] = 'X' 
            elif grid[robot_guess_x] == 'J': 
                rowJ1[int(grid1[robot_guess_y]) - 1] = 'X' 
display_board()                                                                                       # Display the board 
battleship = pick_battleship()                                                                        # Have the user pick the location of their battleship and store it as a list in the variable, battleship 
play_game()                                                                                           # Have the user and the opponent compete against each other in the game of Battleship 