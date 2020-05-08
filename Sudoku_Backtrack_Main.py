
# A Backtracking program  in Python to solve Sudoku problem 
# The code has been contributed by Harshit Sidhwa and modified and adapted by Lucky Gerona.

          
# Function to Find the entry in the Grid that is still  not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remains, false is returned. 
# 'temporary_solution' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
def find_empty_location(arr,temporary_solution):

    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                temporary_solution[0]=row 
                temporary_solution[1]=col 
                return True
    return False
  
# Returns a true/false bool to check if entry is allowable
# in the specified row matches the given number. 
def already_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
# Returns a true/false bool to check if entry is allowable
# in the specified column matches the given number. 
def already_in_column(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
# Returns a true/false bool to check if entry is allowable
# within the specified 3x3 box matches the given number 
def already_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  
# Checks all possible conflicts. Returns a true/false bool which indicates whether it will be legal to assign num to the given row,col location. 
def check_location_is_safe(arr,row,col,num): 
      
    # Check if 'num' is not already placed in current row, current column and current 3x3 box 
    return not already_in_row(arr,row,num) and not already_in_column(arr,col,num) and not already_in_box(arr,row - row%3,col - col%3,num) 
  

# Recursive function to check an input grid and tries to brute force all possible answers
def solve_sudoku(arr):       
    # 'temporary_solution' is a list variable that keeps the record of row and col in find_empty_location Function     
    temporary_solution=[0,0] 
      
    # if there are no empyty spaces, a solution is achieved 
    if(not find_empty_location(arr,temporary_solution)): 
        return True
      
    # Assigning list values to row and col that we got from the above Function 
    row=temporary_solution[0] 
    col=temporary_solution[1] 
      
    # consider digits 1 to 9 (brute force part)
    for num in range(1,10): 
          
        # check if the number is allowed to be placed
        if(check_location_is_safe(arr,row,col,num)): 
            # TRY
            arr[row][col]=num
            # Call function again 
            if(solve_sudoku(arr)):
                return True
            # if a conflict arises, recursions is popped and the trial is reverted, previous entries are  reverted also. next number is choses 
            arr[row][col] = 0
              
    # Backtracking, pops off recursions         
    return False 

# Convert data from the input window dictionary into an int matrix
def convert_input_data(input_natin,grid_natin):
    print(grid_natin)
    for x in range(0,80):
        # 0-9 column
        column_values = int(x%9)
        # 0-9 row
        row_values =  int(x/9)
        # index the dictionary and change into a matrix 
        if values[x] != '':
            # typecast to int if input is seen
            grid_natin[row_values,column_values] = int(values[x])
        else:
            # zero elsewise
            grid_natin[row_values,column_values] = 0
    return grid_natin





################################################
#             Sudoku Puzzle Input              #
################################################


import PySimpleGUI as sg
import numpy as np
import time

# Setup input window
headings = ['', '', '','', '', '', '', '', '']
header =  [[sg.Text('  ')] + [sg.Text(h, size=(1,1), justification='center') for h in headings]]

input_rows = [[sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)],
                [sg.Input(size=(4,12), pad=(1,1)) for col in range(9)]]

layout = header + input_rows + [[sg.Submit(),sg.Cancel()]]

window = sg.Window('Sudoku Input', layout, font='Courier 12')
# Read the window
event, values = window.read()






# values is a Dictionary. Use brackets with numbers as keys
grid_natin = np.zeros((9,9), dtype=int)
grid_natin = convert_input_data(values,grid_natin)

# Print initial grid configuration 
print(grid_natin)




###########################################################
#       Driver main function to test above functions      #
###########################################################

if __name__=="__main__": 
      
    # start recursion and print if a solution exists 
    if(solve_sudoku(grid_natin)): 
        # Print final and solved configuration
        print(grid_natin) 
    else: 
        print ("No solution exists")
  