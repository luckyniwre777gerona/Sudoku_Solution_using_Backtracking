
# A Backtracking program  in Python to solve Sudoku problem 
  
  
# A Utility Function to print the Grid 
def print_grid(arr): 
    
    BOX_SIZE = 25

    layout = [
                [sg.Text('SOLVING SUDOKU PUZZLE'), sg.Text('', key='_OUTPUT_')],
                [sg.Graph((800,800), (0,250), (250,0), key='_GRAPH_')],
                [sg.Button('Show'), sg.Button('Exit')]
             ]

    window = sg.Window('Window Title').Layout(layout).Finalize()

    g = window.FindElement('_GRAPH_')

    for row in range(9):
        for i in range(9):
            g.DrawRectangle((i*BOX_SIZE+5,row*BOX_SIZE+3), (i*BOX_SIZE+BOX_SIZE+5,row*BOX_SIZE+BOX_SIZE+3), line_color='black')
            g.DrawText('{}'.format(arr[row][i]),(i*BOX_SIZE+17.5,row*BOX_SIZE+17))

    time.sleep(1)
    return    
   
          
# Function to Find the entry in the Grid that is still  not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remains, false is returned. 
# 'l' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
def find_empty_location(arr,l):

    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  
# Checks whether it will be legal to assign num to the given row,col 
#  Returns a boolean which indicates whether it will be legal to assign 
#  num to the given row,col location. 
def check_location_is_safe(arr,row,col,num): 
      
    # Check if 'num' is not already placed in current row, 
    # current column and current 3x3 box 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
  
# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(arr): 
      
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0] 
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(arr,l)): 
        return True
      
    # Assigning list values to row and col that we got from the above Function  
    row=l[0] 
    col=l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
          
        # if looks promising 
        if(check_location_is_safe(arr,row,col,num)): 
              
            # make tentative assignment 
            arr[row][col]=num
  
            # return, if success, ya! 
            if(solve_sudoku(arr)):
                
                return True
  
            # failure, unmake & try again 
            arr[row][col] = 0
              
    # this triggers backtracking         
    return False 

def convert_input_data(input_natin,grid_natin):
    print(grid_natin)
    for x in range(0,80):
        column_values = int(x%9)
        row_values =  int(x/9)

        if values[x] != '':
            grid_natin[row_values,column_values] = int(values[x])
        
        else:
            grid_natin[row_values,column_values] = 0

    return grid_natin





################################################
#             Sudoku Puzzle Input              #
################################################


import PySimpleGUI as sg
import numpy as np
import time

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
event, values = window.read()




# values is a Dictionary. USe brackets with numbers as keys




grid_natin = np.zeros((9,9), dtype=int)
grid_natin = convert_input_data(values,grid_natin)





###########################################################
#       Driver main function to test above functions      #
###########################################################

if __name__=="__main__": 
      
    # if success print the grid 
    if(solve_sudoku(grid_natin)): 
        print(grid_natin) 
    else: 
        print ("No solution exists")
  
# # The above code has been contributed by Harshit Sidhwa.
window.close()




BOX_SIZE = 25

layout = [
    [sg.Text('SOLVING SUDOKU PUZZLE'), sg.Text('', key='_OUTPUT_')],
    [sg.Graph((800,800), (0,250), (250,0), key='_GRAPH_')],
    [sg.Button('Show'), sg.Button('Exit')]
    ]

window = sg.Window('Window Title').Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

for row in range(9):
    for i in range(9):
        g.DrawRectangle((i*BOX_SIZE+5,row*BOX_SIZE+3), (i*BOX_SIZE+BOX_SIZE+5,row*BOX_SIZE+BOX_SIZE+3), line_color='black')
        g.DrawText('{}'.format(grid_natin[row][i]),(i*BOX_SIZE+17.5,row*BOX_SIZE+17))
window.read()


