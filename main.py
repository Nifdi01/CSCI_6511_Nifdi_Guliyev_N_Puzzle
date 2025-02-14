from n_puzzle import NPuzzle
from utils import read_puzzle
import sys

def main():
    """
    Main function to run the NPuzzle solver.

    This function performs the following steps:
      1. Reads the puzzle configuration from the file 'n-puzzle.txt'.
      2. Processes command-line arguments to determine which heuristic to use:
         - 'm' for Manhattan (default)
         - 'e' for Euclidean
      3. Initializes the NPuzzle instance with the given configuration.
      4. Attempts to solve the puzzle using the NPuzzle solver.
      5. Prints the number of moves to reach the solution or a message if no solution is found.
    """
    # Define the file path for the puzzle configuration
    file_path = 'n-puzzle.txt'
    
    # Attempt to read the puzzle configuration from file
    try:
        initial_state = read_puzzle(file_path)
    except Exception as e:
        print(f"Error reading puzzle file: {e}")
        return
    
    # Process command-line argument for heuristic selection
    try:
        heuristic = sys.argv[1]
        # Validate that the provided heuristic is either 'm' (Manhattan) or 'e' (Euclidean)
        if heuristic not in "me":
            print("No such heuristic")
            print("Usage:")
            print(" e - Euclidean\n m (default) - Manhattan")
            return
    except IndexError:
        # If no heuristic argument is provided, default to Manhattan ('m')
        heuristic = "m"

    # Attempt to initialize the NPuzzle with the initial state and chosen heuristic
    try:
        puzzle = NPuzzle(initial_state, heuristic=heuristic)
    except ValueError as ve:
        print(f"Invalid puzzle configuration: {ve}")
        return

    # Solve the puzzle and capture the solution cost (number of moves)
    solution = puzzle.solve()
    if solution != -1:
        print("Solution found in", solution, "moves")
    else:
        print("No solution found.")
        
        
if __name__ == "__main__":
    main()