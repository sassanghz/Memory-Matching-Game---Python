'''
Author: Sassan Ghazi
Date: 2024-11-6
Course: COMP - 348
'''

#IMPORTED PACKAGES
import random

#CLASS 
class memory_grid:
    # CONSTRUCTOR
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.pairsCount = (gridSize ** 2) // 2
        self.hiddenGrid = [['X' for _ in range(gridSize)] for _ in range(gridSize)]
        self.grid = self._generate_grid()
        self.foundPairs = 0
        self.attemps = 0
    
    def _generate_grid(self):
        elements_grid = [i // 2 for i in range(self.gridSize * self.gridSize)]
        
        #shuffle the grid elements whenever generated
        for i in range(len(elements_grid) - 1, 0, 1):
            j = random.randint(0,i)
            elements_grid[i], elements_grid[j] = elements_grid[j], elements_grid[i]
        
        #list turns in a grid for display
        return [elements_grid[i * self.gridSize:(i + 1) * self.gridSize] for i in range(self.gridSize)]

    def element_cell_reveal(self, row1, col1, row2, col2):
        self.attemps += 1

        if self.grid[row1][col1] == self.grid[row2][col2]:
            # elements matched
            self.hiddenGrid[row1][col1] = str(self.grid[row1][col1])
            self.hiddenGrid[row2][col2] = str(self.grid[row2][col2])
            self.foundPairs += 1
            return True
        else:
            # elements != match
            return False
    
    def element_cell_hidden(self, row1, col1, row2, col2):
        self.hiddenGrid[row1][col2] = 'X'
        self.hiddenGrid[row2][col2] = 'X'
    
    def game_over(self):
        # if all elements have been found
        return self.foundPairs == self.pairsCount
    
    def display_grid(self):
        header = "  "
        
        for i in range(self.gridSize):
            #Appending each column letter with a space
            header += chr(65 + i) + " "
        print(header.strip())

        #each row is printed with row indices
        index_row = 0

        for row in self.element_cell_hidden:
            # Lines start with the row index in brackets
            row_line = f"[{index_row}]"

            for cell in row:
                #Append each cell with a space
                row_line += cell + " "
            print(row_line.strip())
            index_row += 1
    
    def final_score(self):
        print(f"\nCongratulations! You've won! ")



