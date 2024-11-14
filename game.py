'''
Author: Sassan Ghazi
Date: 2024-11-6
Course: COMP - 348
'''

#IMPORTED PACKAGES
import sys
import random
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
    choice = 0
    while True:
        menu_displayment()
        grid_init.display_grid()

        if choice == '1':
            user_guess = input("\nEnter cell coordinates (e.g., a0): ")
            user_guess2 = input("Enter cell coordinates (e.g., b0): ")
        
            try:
                row1, col1 = int(user_guess[0].upper()) - 65
                row2, col2 = int(user_guess2[0].upper()) - 65

                if not (0 <= gridSize and 0 <= col1 < gridSize and 0 <= row2 < gridSize and 0 <= col2 < gridSize):
                
                    print("Input Error: column entry is out of range for this grid. Please try again.")
                    continue

                if grid_init.element_cell_reveal(row1, col1, row2, col2):
                    print("matching elements")
                else:
                    print("no match")
                    grid_init.element_cell_hidden(row1, col1, row2, col2)
            
            except (IndexError, ValueError):
                print("Input Error: column entry is out of range for this grid. Please try again.")
                continue

        elif choice == '2':
            #revealing one element as a hint
            row, col = divmod(random.randint(0, gridSize * gridSize - 1), gridSize)
            print(f"Uncovered element at ({chr(65 + col)}{row}): {grid_init.grid[row][col]}")
            grid_init.element_cell_hidden[row][col] = str(grid_init.grid[row][col])
        
        elif choice == '3':
            #reveal the full grid 
            print("\nFull Grid Displayed:")
            for row in grid_init.grid:
                print(" ".join(str(cell) for cell in row))
            break
        
if __name__ == '__main__':
    main()

