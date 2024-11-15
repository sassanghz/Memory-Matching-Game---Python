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
        self.attempts = 0
        self.actual_guesses = 0
        self.minimum_potential_guesses = self.pairsCount
    
    def _generate_grid(self):
        elements_grid = [i // 2 for i in range(self.gridSize * self.gridSize)]
        
        #shuffle the grid elements whenever generated
        for i in range(len(elements_grid) - 1, 0, -1):
            j = random.randint(0,i)
            elements_grid[i], elements_grid[j] = elements_grid[j], elements_grid[i]
        
        #list turns in a grid for display
        return [elements_grid[i * self.gridSize:(i + 1) * self.gridSize] for i in range(self.gridSize)]

    def element_cell_reveal(self, row1, col1, row2, col2):
        self.attempts += 1
        self.actual_guesses += 1

        if self.hiddenGrid[row1][col1] != 'X' or self.hiddenGrid[row2][col2] != 'X':
            # If either cell is already revealed, do not proceed and return False
            print("One or both cells are already revealed.")
            return False

        if self.grid[row1][col1] == self.grid[row2][col2]:
            # elements matched
            self.hiddenGrid[row1][col1] = str(self.grid[row1][col1])
            self.hiddenGrid[row2][col2] = str(self.grid[row2][col2])
            self.foundPairs += 1
            return True
        else:
            # elements != match
            self.hiddenGrid[row1][col1] = str(self.grid[row1][col1])
            self.hiddenGrid[row2][col2] = str(self.grid[row2][col2])
            return False
    
    def element_cell_hidden(self, row1, col1, row2, col2):
        self.hiddenGrid[row1][col1] = 'X'
        self.hiddenGrid[row2][col2] = 'X'
    
    def option2_guesses(self):
        self.actual_guesses += 2
    
    def calculate_score(self):
        if self.actual_guesses == 0:
            return 0
        return (self.minimum_potential_guesses / self.actual_guesses) * 100
    
    def uncover_element(self):
        # find the hidden cells marked as x
        hidden_cells = [(r,c) for r in range(self.gridSize) for c in range(self.gridSize) if self.hiddenGrid[r][c] == 'X']

        if hidden_cells:
            row, col = random.choice(hidden_cells)
            self.hiddenGrid[row][col] = str(self.grid[row][col])
        else:
            print("Due to using the cheating method. Your score is {}")

    def reveal_grid(self):
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                self.hiddenGrid[row][col] = str(self.grid[row][col])

    def display_grid(self):
        #title with borders
        print("--------------------")
        print("|   Brain Buster   |")
        print("--------------------\n")

        header = ""  # Space to align with row indices
        for i in range(self.gridSize):
            # Append each column letter in brackets with spaces for alignment
            header += f"[{chr(65 + i)}]" + "  "
        print(header.strip())


        # Print each row with row indices
        index_row = 0
        for row in self.hiddenGrid:
            # Start each line with the row index in brackets
            row_line = f"[{index_row}] "
            for cell in row:
                # Append each cell with two spaces for alignment
                row_line += f" {cell}   "
            print(row_line.strip())
            index_row += 1
