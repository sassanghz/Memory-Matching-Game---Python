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

    


