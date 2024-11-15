'''
Author: Sassan Ghazi
Date: 2024-11-6
Course: COMP - 348
'''

#IMPORTED PACKAGES
import os
import sys
import random
import time
#IMPORTED CLASS
from grid import memory_grid

# Function Definitions
def options_displayment():
    print("\n1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit")
    return input("\nSelect: ")

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


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
        sys.exit(1)
    
    #start the game
    grid_init = memory_grid(gridSize)

    while True:
        clear_screen()
        grid_init.display_grid()

        choice = options_displayment()

        if choice == '1':
            # Get coordinates for the first and second cell from the user
            user_guess = input("\nEnter coordinates of the first cell (e.g., A0): ")
            user_guess2 = input("Enter coordinates of the second cell (e.g., B1): ")
            
            try:
                # Convert input into row and column indices
                row1, col1 = int(user_guess[1]), ord(user_guess[0].upper()) - 65
                row2, col2 = int(user_guess2[1]), ord(user_guess2[0].upper()) - 65

                # Check if indices are within bounds
                if not (0 <= row1 < gridSize and 0 <= col1 < gridSize and 
                        0 <= row2 < gridSize and 0 <= col2 < gridSize):
                    print("Input Error: One or both coordinates are out of range for this grid. Please try again.")
                    continue

                # Attempt to reveal the cells
                if grid_init.element_cell_reveal(row1, col1, row2, col2):
                    print("It's a match!")

                else:
                    grid_init.display_grid()  # Show the grid with the temporarily revealed cells
                    time.sleep(2)  # Wait for 2 seconds
                    grid_init.element_cell_hidden(row1, col1, row2, col2)  # Hide the cells again
                    grid_init.display_grid()  # Re-display the grid after hiding the cells

            except (IndexError, ValueError):
                print("Input Error: Invalid input format. Please enter coordinates like A0 or B1.")
                continue


        elif choice == '2':
            #revealing one element as a hint
            grid_init.uncover_element()
            grid_init.option2_guesses()
        
        elif choice == '3':
            #turn all the hidden elements into revealed elements the full grid 
            grid_init.reveal_grid()
            #display the revealed grid
            grid_init.display_grid()
            #display the score
            score = grid_init.calculate_score()
            print(f"\nDue to using the cheating method. Your score is {score:.1f}")
            break

        elif choice == '4':
            #new game
            print("Starting a new game!")
            grid_init = memory_grid(gridSize)
        
        elif choice == '5':
            print("Exiting the game...")
            break

        else:
            print("Invalid selection.")
            time.sleep(2)

        # Check if the game is over (all pairs matched)
        if grid_init.foundPairs == grid_init.pairsCount:
            score = grid_init.calculate_score()
            print("\nCongratulations! You've matched all pairs!")
            print(f"Your score is: {score:.1f}")
            break

if __name__ == '__main__':
    main()