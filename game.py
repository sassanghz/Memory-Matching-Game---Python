'''
Author: Sassan Ghazi
Date: 2024-11-6
Course: COMP - 348
'''

#IMPORTED PACKAGES
import sys
#IMPORTED CLASS
from grid import memory_grid

# Function Definitions
def menu_displayment():
    print("--------------------")
    print("|    Brain Buster  |")
    print("--------------------")
    print("\n[A] [B] [C] [D]")

def options_displayment():
    print("\n1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit")
    return input("\nSelect: ")


#MAIN
def main():
    #command line argument for grid size
    if len(sys.argv) != 2:
        print("Usage: python game.py <gridSize>")
        print("Choose gridSize as 2 | 4 | 6")
        sys.exit(1)

    #generating the grid size
    try:
        gridSize = int(sys.argv[1])
        if gridSize not in [2,4,6]:
            raise ValueError
    except ValueError:
        print("Invalid grid size. User must choose ")
    
    #start the game
    grid_init = memory_grid(gridSize)
    
    while True:
        menu_displayment()
        

if __name__ == '__main__':
    main()

