from typing import List, Tuple

from typing import List

def read_puzzle(file_path: str) -> List[List[int]]:
    """
    Reads a sliding puzzle configuration from a text file and returns it as a 2D list.
    
    Each line in the file is assumed to represent a row of the puzzle. Tokens in each line 
    are separated by whitespace. Tokens that are digits are converted to integers; any non-digit 
    token is interpreted as 0 (representing the blank tile).
    
    After reading, each row is padded with zeros on the left if it has fewer elements than the 
    number of rows, ensuring the puzzle is an n x n matrix. If a row has more than n elements, 
    a ValueError is raised. Additionally, the function ensures that 3 <= n <= 6.
    
    Parameters:
        file_path (str): The path to the puzzle file.
    
    Returns:
        List[List[int]]: A 2D list representing the puzzle state.
    
    Raises:
        ValueError: If the puzzle size is not within the allowed range (3 <= n <= 6) or 
                    if any row does not have the expected number of elements after padding.
    """
    puzzle: List[List[int]] = []

    # Open and read the file line by line
    with open(file_path) as file:
        for line in file:
            # Remove trailing newline characters and split the line into tokens
            tokens = line.rstrip("\n").split()
            # Convert each token to an integer if it's a digit; otherwise, use 0
            row = [int(token) if token.isdigit() else 0 for token in tokens]
            puzzle.append(row)

    n = len(puzzle)  # The expected number of elements per row based on the number of rows

    # Enforce the constraint 3 <= n <= 6
    if not (3 <= n <= 6):
        raise ValueError(f"Invalid puzzle size: {n}x{n}. Puzzle size must be between 3 and 6.")

    # Pad rows with fewer elements than n by inserting zeros at the beginning
    for idx, row in enumerate(puzzle):
        while len(row) < n:
            row.insert(0, 0)
        if len(row) != n:
            raise ValueError(f"Row {idx+1} has {len(row)} elements but expected {n}.")

    return puzzle


def generate_goal_state(n: int) -> Tuple[Tuple[int, ...], ...]:
    """
    Generates the goal state for an n x n sliding puzzle.
    
    The goal state is represented as a tuple of tuples (for immutability), where the tiles 
    are filled in row-major order from 1 to n*n - 1, and the blank tile (0) is placed at the 
    end. The modulo operation ensures that the last element becomes 0.
    
    Parameters:
        n (int): The dimension of the puzzle (n x n).
    
    Returns:
        Tuple[Tuple[int, ...], ...]: The goal state of the puzzle as an immutable tuple-of-tuples.
    """
    # Create the goal state using list comprehension
    goal = [[(i * n + j + 1) % (n * n) for j in range(n)] for i in range(n)]
    # Convert the list of lists into a tuple of tuples for immutability
    return tuple(tuple(row) for row in goal)

def find_blank(state: List[List[int]], n: int) -> Tuple[int, int]:
    """
    Finds the position of the blank tile (represented by 0) in the puzzle state.
    
    Iterates through the state row by row and column by column. If the blank tile is found,
    its (row, column) coordinates are returned. If the blank tile is not found, (-1, -1) is returned.
    
    Parameters:
        state (List[List[int]]): The current state of the puzzle as a 2D list.
        n (int): The dimension of the puzzle (n x n).
    
    Returns:
        Tuple[int, int]: The (row, column) position of the blank tile, or (-1, -1) if not found.
    """
    # Iterate over each row and column in the state
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                return i, j  # Return the coordinates of the blank tile
    return -1, -1  # Return (-1, -1) if no blank tile is found