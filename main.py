from n_puzzle import NPuzzle
from utils import read_puzzle
import sys

def main():
    file_path = 'n-puzzle.txt'
    try:
        initial_state = read_puzzle(file_path)
    except Exception as e:
        print(f"Error reading puzzle file: {e}")
        return
    
    heuristic = sys.argv[1]

    try:
        puzzle = NPuzzle(initial_state, heuristic=heuristic)
    except ValueError as ve:
        print(f"Invalid puzzle configuration: {ve}")
        return

    solution = puzzle.solve()
    if solution!=-1:
        print("Solution found in", solution, "moves:")
    else:
        print("No solution found.")
        
    
if __name__ == '__main__':
    main()