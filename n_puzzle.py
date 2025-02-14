from queue import PriorityQueue
from heuristics import *
from utils import generate_goal_state, find_blank

class NPuzzle:
    def __init__(self, initial_state, heuristic="m"):
        self.n = len(initial_state)
        for idx, row in enumerate(initial_state):
            if len(row) != self.n:
                raise ValueError(
                    f"Row {idx+1} has {len(row)} elements but each row must have {self.n} elements with empty tab representing the blank."
                )
        self.initial_state = tuple(tuple(row) for row in initial_state)
        if heuristic == "e":
            print("Using Euclidean")
            self.heuristic = euclidean
        elif heuristic == "m":
            print("Using Manhattan")
            self.heuristic = manhattan
        self.goal_state = generate_goal_state(self.n)
        
    def get_neighbors(self, state):
        blank_i, blank_j = find_blank(state, self.n)
        neighbors = []
        
        moves = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]
        
        for di, dj, move in moves:
            new_i, new_j = blank_i + di, blank_j + dj
            if 0 <= new_i < self.n and 0 <= new_j < self.n:
                new_state = [list(row) for row in state]
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                neighbors.append(tuple(tuple(row) for row in new_state))
        return neighbors
    
    def solve(self):
        priority_queue = PriorityQueue()
        initial_heuristic = self.heuristic(self.n, self.initial_state)
        priority_queue.put((initial_heuristic, 0, self.initial_state))
        
        visited = set()
        nodes_expanded = 0  # Counter for nodes expanded
        
        while not priority_queue.empty():
            _, cost, current_state = priority_queue.get()
            nodes_expanded += 1  # Increment counter each time we pop a node
            
            if current_state == self.goal_state:
                print("Nodes Expanded:", nodes_expanded)
                return cost
            
            if current_state in visited:
                continue
            
            visited.add(current_state)
            
            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    new_cost = cost + 1
                    h = self.heuristic(self.n, neighbor)
                    priority_queue.put((new_cost + h, new_cost, neighbor))

        print("Nodes Expanded:", nodes_expanded)
        return -1
