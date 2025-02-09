from typing import List


def read_puzzle(file_path):
    puzzle = list()
    with open(file_path) as file:
        for line in file:
            tokens = line.rstrip("\n").split()
            row = [int(token) if token.isdigit() else 0 for token in tokens]
            puzzle.append(row)
            
    n = len(puzzle)
    
    for idx, row in enumerate(puzzle):
        while len(row) < n:
            row.insert(0, 0)
        if len(row) != n:
            raise ValueError(f"Row {id+1} has {len(row)} elements but expected {n}.")
    
    return puzzle
        