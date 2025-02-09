from utils import generate_goal_state, find_blank

class NPuzzle:
    def __init__(self, initial_state):
        self.n = len(initial_state)
        for idx, row in enumerate(initial_state):
            if len(row) != self.n:
                raise ValueError(
                    f"Row {idx+1} has {len(row)} elements but each row must have {self.n} elements with empty tab representing the blank."
                )
        self.initial_state = tuple(tuple(row) for row in initial_state)
        self.goal_state = generate_goal_state(self.n)
        
    def get_neighbors(self, state):
        blank_i, blank_j = find_blank(state, self.n)
        neighbors = list()
        
        moves = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]
        
        for di, dj, move in moves:
            new_i, new_j = blank_i + di, blank_j + dj
            if 0 <= new_i < self.n and 0 <= new_j < self.n:
                new_state = list(list(row) for row in state)
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                neighbors.append((tuple(tuple(row) for row in new_state), move))
        return neighbors
    
    
