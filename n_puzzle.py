from queue import PriorityQueue
from heuristics import *
from utils import generate_goal_state, find_blank

class NPuzzle:
    """
    Class representing an n x n sliding puzzle and providing methods to solve it using A* search.
    
    Attributes:
        n (int): The dimension of the puzzle.
        initial_state (tuple of tuples): The immutable initial puzzle configuration.
        heuristic (function): The heuristic function to estimate distance to the goal.
        goal_state (tuple of tuples): The goal configuration of the puzzle.
    """
    
    def __init__(self, initial_state, heuristic="m"):
        """
        Initialize the NPuzzle instance with the given initial state and heuristic choice.
        
        The initial state is validated to ensure that it is an n x n matrix. The puzzle state is 
        converted to an immutable tuple-of-tuples. The chosen heuristic function is set based on 
        the input ("m" for Manhattan, "e" for Euclidean). If an invalid heuristic is provided, 
        it defaults to Manhattan.
        
        Parameters:
            initial_state (list of lists of int): The starting configuration of the puzzle.
            heuristic (str, optional): The heuristic type: "m" for Manhattan (default) or "e" for Euclidean.
        
        Raises:
            ValueError: If any row in the initial state does not contain exactly n elements.
        """
        self.n = len(initial_state)
        # Validate that each row has exactly n elements
        for idx, row in enumerate(initial_state):
            if len(row) != self.n:
                raise ValueError(
                    f"Row {idx+1} has {len(row)} elements but each row must have {self.n} elements with empty tab representing the blank."
                )
        # Convert the initial state to an immutable tuple-of-tuples
        self.initial_state = tuple(tuple(row) for row in initial_state)
        
        # Choose the heuristic function based on the provided argument
        if heuristic == "e":
            print("Using Euclidean")
            self.heuristic = euclidean
        elif heuristic == "m":
            print("Using Manhattan")
            self.heuristic = manhattan
        else:
            # Default to Manhattan if the input is not recognized
            print("Unknown heuristic provided, defaulting to Manhattan")
            self.heuristic = manhattan
        
        # Generate the goal state for the puzzle
        self.goal_state = generate_goal_state(self.n)
        
    def get_neighbors(self, state):
        """
        Generate all valid neighboring states by moving the blank tile in the current state.
        
        The blank tile (represented by 0) is moved up, down, left, or right if possible. Each valid 
        move results in a new puzzle state, which is returned as an immutable tuple-of-tuples.
        
        Parameters:
            state (tuple of tuples): The current puzzle configuration.
        
        Returns:
            list of tuples: A list of neighboring puzzle states.
        """
        # Locate the blank tile (0) in the current state
        blank_i, blank_j = find_blank(state, self.n)
        neighbors = []
        
        # Define possible moves: (row offset, column offset, move description)
        moves = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]
        
        # Try each possible move
        for di, dj, move in moves:
            new_i, new_j = blank_i + di, blank_j + dj
            # Check if the new position is within puzzle boundaries
            if 0 <= new_i < self.n and 0 <= new_j < self.n:
                # Create a mutable copy of the current state to perform the swap
                new_state = [list(row) for row in state]
                # Swap the blank tile with the adjacent tile
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                # Convert the state back to an immutable tuple-of-tuples and add to neighbors list
                neighbors.append(tuple(tuple(row) for row in new_state))
        return neighbors
    
    def solve(self):
        """
        Solve the sliding puzzle using the A* search algorithm.
        
        The method uses a priority queue to explore states based on the sum of the path cost 
        and heuristic value. The search continues until the goal state is reached, and the number 
        of moves (cost) is returned. Additionally, the number of nodes expanded during the search 
        is printed for analysis. If no solution exists, -1 is returned.
        
        Returns:
            int: The number of moves to reach the goal state, or -1 if the puzzle is unsolvable.
        """
        # Initialize the priority queue; each item is a tuple (priority, cost, state)
        priority_queue = PriorityQueue()
        initial_heuristic = self.heuristic(self.n, self.initial_state)
        priority_queue.put((initial_heuristic, 0, self.initial_state))
        
        visited = set()  # Set to track visited states and avoid revisiting
        nodes_expanded = 0  # Counter for the number of nodes expanded during the search
        
        # A* search loop: process nodes until the queue is empty or the goal is reached
        while not priority_queue.empty():
            _, cost, current_state = priority_queue.get()
            nodes_expanded += 1  # Increment the expansion counter
            
            # Check if the goal state has been reached
            if current_state == self.goal_state:
                print("Nodes Expanded:", nodes_expanded)
                return cost
            
            # Skip processing if the current state has already been visited
            if current_state in visited:
                continue
            
            # Mark the current state as visited
            visited.add(current_state)
            
            # Process all valid neighboring states
            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    new_cost = cost + 1  # Increment path cost for the move
                    # Calculate the heuristic for the neighbor
                    h = self.heuristic(self.n, neighbor)
                    # Add the neighbor to the queue with priority as cost + heuristic
                    priority_queue.put((new_cost + h, new_cost, neighbor))
        
        # If the queue is exhausted without finding a solution, output the nodes expanded and return -1
        print("Nodes Expanded:", nodes_expanded)
        return -1