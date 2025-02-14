import math

def manhattan(n, state):
    """
    Calculate the Manhattan distance heuristic for a sliding puzzle.

    The Manhattan distance is the sum of the absolute differences between the current position 
    and the target position (row and column) of each tile. The blank tile (represented by 0) is ignored.

    Parameters:
        n (int): The dimension of the puzzle (n x n).
        state (list of list of int): The current state of the puzzle represented as a 2D list, where 
                                     each element corresponds to a tile (0 represents the blank).

    Returns:
        int: The total Manhattan distance for the puzzle state.
    """
    distance = 0  # Initialize total distance to 0
    
    # Iterate over each row
    for i in range(n):
        # Iterate over each column in the current row
        for j in range(n):
            val = state[i][j]  # Current tile value
            # Skip the blank tile (represented by 0)
            if val != 0:
                # Calculate the target (goal) position for the current tile
                target_i, target_j = (val - 1) // n, (val - 1) % n
                # Compute Manhattan distance (vertical + horizontal distance)
                distance += abs(target_i - i) + abs(target_j - j)
    return distance

def euclidean(n, state):
    """
    Calculate the Euclidean distance heuristic for a sliding puzzle.

    The Euclidean distance is the straight-line distance between the current position and the target 
    position of each tile. The blank tile (represented by 0) is ignored.

    Parameters:
        n (int): The dimension of the puzzle (n x n).
        state (list of list of int): The current state of the puzzle represented as a 2D list, where 
                                     each element corresponds to a tile (0 represents the blank).

    Returns:
        float: The total Euclidean distance for the puzzle state.
    """
    distance = 0  # Initialize total distance to 0
    
    # Iterate over each row
    for i in range(n):
        # Iterate over each column in the current row
        for j in range(n):
            val = state[i][j]  # Current tile value
            # Skip the blank tile (represented by 0)
            if val != 0:
                # Calculate the target (goal) position for the current tile
                target_i, target_j = (val - 1) // n, (val - 1) % n
                # Compute Euclidean distance (straight-line distance) and add to total
                distance += math.sqrt((target_i - i)**2 + (target_j - j)**2)
    return distance