"""
Requirements: 
1. Print Grid such that it outputs like:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
2. asdf

Source: https://automatetheboringstuff.com/chapter4/ -> search for Character Picture Grid
"""

# Define grid: A List that contains Lists
heartGrid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Debug initial print of grid
# print(str(heartGrid))

# Define String variables to hold the grid
gridRow = len(heartGrid)                   # gridRow == The # of Indices in heartGrid's Parent List Reference
gridColumn = len(heartGrid[0])             # gridColumn == The # of Indices in one of heartGrid's nested List's

# Define a function to print the Grid v2
def printGrid(gridList):
    # Iterate through Columns 1st
    for y in range(gridColumn):
            # Then iterate through Rows 2nd
            for x in range(gridRow):
                # Print the present X and Y Index values
                print(gridList[x][y], end='')
            # Print a New Line after each Column has been Printed
            print()

# Print heartGrid using the printGrid function
printGrid(heartGrid)
