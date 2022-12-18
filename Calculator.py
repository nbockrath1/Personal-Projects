# Author: Nicholas Bockrath 
# Date of Creation: 20221217 
# Description: Repeatedly prompt the user for an equation until they type 'done', and accurately calculate each equation entered. 
while True: 
    i = input('Enter Equation: ') # Store the user's equation into the variable i 
    if i == 'done':               # Halt the program when the user types 'done' 
        break 
    div = i.split()               # Divide the user's input into its parts and store it in the form of a list in the variable div 
    if div[0] == '(':             # Account for an equation being stored in parantheses on the left side of the operator (Ex: ( 3 - 2 ) + 1) 
        div.pop(0)                # Remove the parantheses from div 
        div.pop(3) 
        try:                      # If possible, store the equation in the parantheses into float variables, and remove it from div 
            x = float(div[0]) 
            op = div[1] 
            y = float(div[2]) 
            div.pop(0) 
            div.pop(0) 
            div.pop(0) 
        except:                   # If the operands cannot be stored as float variables, then alert the user of an error and restart the loop 
            print('Error') 
            continue 
        if div[1] == '(':         # If a second equation inside parantheses is found on the right side of the operator, then rearrange the div list so the first equation can be replaced with its answer without altering the indexes of the second equation 
            div.append(div[5]) 
            div[5] = div[4] 
            div[4] = div[3] 
            div[3] = div[2] 
            div[2] = div[1] 
            div[1] = div[0] 
            if op == '+': 
                div[0] = (x+y) 
            elif op == '-': 
                div[0] = (x-y) 
            elif op == '*': 
                div[0] = (x*y) 
            elif op == '/': 
                div[0] = (x/y) 
            elif op == '^': 
                div[0] = (x**y) 
            else: 
                print('Error') 
        else:                     # If no second equation bounded by parantheses is found, then replace the bounded equation with its answer 
            div.append(div[1]) 
            div[1] = div[0] 
            if op == '+': 
                div[0] = (x+y) 
            elif op == '-': 
                div[0] = (x-y) 
            elif op == '*': 
                div[0] = (x*y) 
            elif op == '/': 
                div[0] = (x/y) 
            elif op == '^': 
                div[0] = (x**y) 
            else: 
                print('Error') 
    if div[2] == '(':             # Account for an equation being stored in parantheses on the right side of the operator (Ex: 1 + ( 2 - 3 )) 
        div.pop(2)                # Remove the parantheses 
        div.pop(5) 
        try:                      # If possible, store the equation into float variables and remove the equation from the div list 
            x = float(div[2]) 
            op = div[3] 
            y = float(div[4]) 
            x1 = div[0] 
            op1 = div[1] 
            div.pop(2) 
            div.pop(2) 
            div.pop(2) 
        except:                   # If the equation cannot be stored into float variables, then alert the user of an error and restart the loop 
            print('Error') 
            continue 
        div.append(div[1])        # Alter the div list to prepare the replacement of the bounded equation with its answer 
        if op == '+': 
            div[2] = (x+y) 
        elif op == '-': 
            div[2] = (x-y) 
        elif op == '*': 
            div[2] = (x*y) 
        elif op == '/': 
            div[2] = (x/y) 
        elif op == '^': 
            div[2] = (x**y) 
        else: 
            print('Error') 
    try:                          # If possible, convert each operand to a float number 
        x = float(div[0]) 
        op = div[1] 
        y = float(div[2]) 
    except:                       # If either of the operands can't be converted to a float number, then alert the user and restart the loop 
        print('Error') 
        continue 
    if op == '+':                 # If the operator is a plus sign, then add the operands to each other and print the sum 
        print(x+y) 
    elif op == '-':               # If the operator is a minus sign, then subtract the right operand from the left operand and print the difference 
        print(x-y) 
    elif op == '*':               # If the operator is an asterisk, then multiply the two operands and print the product 
        print(x*y) 
    elif op == '/':               # If the operator is a slash, then divide the left operand by the right operand and print the quotient 
        print(x/y) 
    elif op == '^':               # If the operator is an arrow, then power the left operand by the right operand and print the result 
        print(x**y) 
    else:                         # If the operator is something other than a plus sign, minus sign, asterisk, slash, or arrow, then alert the user of an error and restart the loop 
        print('Error') 