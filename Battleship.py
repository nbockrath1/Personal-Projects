# Author: Nicholas Bockrath 
# Date: 20221218 
# Description: Play a game of Battleship with the user. 
grid = ['A','B','C','D','E','F','G','H','I','J'] 
grid1 = ['1','2','3','4','5','6','7','8','9','10'] 
row = ['O','O','O','O','O','O','O','O','O','O'] 
print("Let's play Battleship!") 
def display_board(): 
    print('  ' + ' '.join(grid1)) 
    count = 0 
    while count < 10: 
        print(grid[count] + ' ' + ' '.join(row)) 
        count += 1 
display_board() 

 