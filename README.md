#### By Nifdi Guliyev

## `NPuzzle` Class
### `NPuzzle` Class Initialization (`__init__`)
The `NPuzzle` class the main component of the program for solving the N-puzzle problem, where the goal is to arrange a set of tiles in a specific order by moving them around. The program has the following methods:
- `__init__(self, initial_state, heuristic="m")`: This is the constructor for the class.
    - `initial_state`: A 2D list representing the initial configuration of the puzzle.
    - `heuristic`: An optional parameter that specifies the heuristic function to use. It can either be "e" for the Euclidean heuristic or any other value for the Manhattan heuristic.
    The initialization process does the following:
    - Checks the size of each row in `initial_state` to ensure they are consistent with the size of the puzzle.
    - Sets `initial_state` to a tuple of tuples to make it immutable.
    - `heuristic` assigns either the Euclidean or Manhattan heuristic to the attribute where Manhattan is the default value.
    - Generates the `goal_state` using the `generate_goal_state` which is part of the `utils`.
### `get_neighbors` Method
This method computes the neighboring states that can be reached from the current state by swapping the blank tile with an adjacent one (left, right, up, or down).
- `get_neighbors(self, state)`:
    - `state`: A tuple of tuples representing the current state of the puzzle.
    - It finds the location of the blank tile by calling `find_blank(state, self.n)`.
    - Then, it iterates over four possible moves: right, left, down, and up (stored in `moves`).
    - For each move, it checks if the new position is valid (within bounds) and generates a new state by swapping the blank tile with its adjacent tile.
    - The resulting states are added to the `neighbors` list, which is returned as a list of possible valid moves.
### `solve` Method
The `solve` method solves the N-puzzle using A_ search_* with a priority queue. A* search combines the current cost (number of moves so far) and the heuristic estimate (estimated distance to the goal).
- `solve(self)`:
    - A priority queue (`priority_queue`) is used to manage the states to explore. It ensures that states with the lowest estimated cost (current cost + heuristic) are explored first.
    - The initial state is inserted into the priority queue with an initial heuristic calculated using the `heuristic` function.
    - A set `visited` keeps track of states that have already been explored to avoid redundant work.
    The search proceeds with the following steps:
    - The method pops the state with the lowest estimated total cost (cost + heuristic) from the priority queue.
    - If the current state is the goal state (`current_state == self.goal_state`), the method returns the cost, which is the number of moves taken to reach the goal.
    - If the state has already been visited, it is skipped.
    - Otherwise, the state is marked as visited, and its neighbors are explored by calling `get_neighbors`.
    - Each neighbor's cost is updated, and the neighbor is added to the priority queue with the total cost (current cost + heuristic).
    - If no solution is found, it returns `-1`.
## Heuristic Functions
The provided code defines two heuristic functions: Manhattan Distance and Euclidean Distance, which are used in the A_ search algorithm_* to estimate the cost of reaching the goal state in the N-puzzle problem.
### `manhattan(n, state)`
The Manhattan Distance heuristic computes the total number of moves required to place each tile in its correct position, assuming it can only move horizontally or vertically.
### How It Works
- `distance = 0`: Initializes the total heuristic cost.
- The function iterates over all positions `(i, j)` in the `state` matrix.
- For each tile `val` (except the blank tile `0`):
    - Computes the target position `(target_i, target_j)` where the tile should be in the goal state.
        - Since the goal state is sequential (1 to n²-1), the target position of `val` is: 
	        $target\_i = (val - 1) / n$
	        $target\_j = (val - 1)mod(n)$
    - Adds the Manhattan Distance to `distance`: $∣target_i−i∣+∣target_j−j∣|target\_i - i| + |target\_j - j|$
- Returns the total sum of distances.
### Example
For a 3×3 puzzle:
```plaintext
Current State:
1  2  3
4  0  5
6  7  8
```
- Tile `5` is at `(1,2)`, but should be at `(1,1)`, so `|1-1| + |1-2| = 1`.
- Tile `7` is at `(2,1)`, but should be at `(2,0)`, so `|2-2| + |0-1| = 1`.
- The total heuristic value is the sum of all these distances.
### `euclidean(n, state)`
The Euclidean Distance heuristic computes the straight-line distance from each tile to its goal position.
### How It Works
- Similar to `manhattan`, but instead of adding absolute distances, it uses the Euclidean formula: $$\large \sqrt{(target\_i - i)^2 + (target\_j - j)^2}$$
- Since the square root operation is expensive, Euclidean distance is less efficient than Manhattan distance for grid-based movement.
### Example
For the same puzzle:
```plaintext
Current State:
1  2  3
4  0  5
6  7  8
```
- Tile `5` moves diagonally from `(1,2)` to `(1,1)`:$\sqrt{(1-1)^2 + (1-2)^2} = \sqrt{1} = 1$
- Tile `7` moves from `(2,1)` to `(2,0)`:$\sqrt{(2-2)^2 + (0-1)^2} = \sqrt{1} = 1$
## Explanation of Helper Functions
Utilities define three helper functions used for handling and processing the N-Puzzle problem:
1. `read_puzzle(file_path)` → Reads a puzzle from a file.
2. `generate_goal_state(n)` → Generates the goal state for an `n × n` puzzle.
3. `find_blank(state, n)` → Finds the position of the blank tile (`0`) in the puzzle.
### `read_puzzle(file_path)`
### Purpose
- Reads an `n × n` puzzle from a file, where numbers are separated by spaces.
- Converts each line into a list of integers.
- Ensures all rows have equal length by padding with `0` if needed.
### How It Works
- Opens the file and reads its lines.
- Splits each line into tokens and converts them into integers.
    - If a token is not a digit, it's converted into `0` (assuming it represents a blank tile).
- Ensures uniform row length by padding with `0` if necessary.
- If any row has more elements than `n`, raises a ValueError.
### Example Input File (`puzzle.txt`)
```
1 2 3
4 5 6
  7 8
```
### Output
```python
[
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]  # Zero added to match the expected 3x3 size
]
```
### `generate_goal_state(n)`
### Purpose
- Creates the goal state of an `n × n` puzzle, where numbers are arranged in order from 1 to n² - 1, with `0` representing the blank space.
### How It Works
- Uses a list comprehension to create the goal state.
- Each tile at position `(i, j)` is assigned a value using: $(i*n+j+1)mod  (n^2)$
- Converts the list into an immutable tuple of tuples.
### Example for `n = 3`
#### Output
```python
(
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)
```
### `find_blank(state, n)`
### Purpose
- Identifies the position `(row, col)` of the blank tile (`0`) in the puzzle.
### How It Works
- Iterates over all elements in `state`.
- If a `0` is found, returns its `(row, col)` index.
- If no `0` is found, returns `(-1, -1)`.
### Example
#### Input
```python
state = (
    (1, 2, 3),
    (4, 0, 5),
    (6, 7, 8)
)
```
#### Output
```python
(1, 1)
```
## Explanation of Helper Functions
### Function: `main()`
### Reads the puzzle from a file
- The puzzle's initial state is read using the `read_puzzle()` function from `utils.py`.
- If an error occurs while reading the file, an exception is caught, and an error message is displayed.
### Parses the heuristic from command-line arguments
- The heuristic is extracted from `sys.argv[1]`.
- If no heuristic is provided, Manhattan (`"m"`) is used by default.
- If the heuristic is not `"m"` (Manhattan) or `"e"` (Euclidean), the program prints an error message and exits.
### Initializes the `NPuzzle` solver
- The `NPuzzle` class is instantiated with the `initial_state` and the selected heuristic.
- If the input puzzle is invalid (e.g., incorrect dimensions), a `ValueError` is raised and caught.
### Solves the puzzle
- Calls `puzzle.solve()` to find the solution using **A*** search.
- If a solution is found, the number of moves required is printed.
- If **no solution** is found, it prints `"No solution found."`.
### Command-Line Usage
To run the script from a terminal:
```sh
python main.py m
```
or
```sh
python main.py e
```
### Heuristic Options

| Flag | Heuristic Type      |
| ---- | ------------------- |
| `m`  | Manhattan (default) |
| `e`  | Euclidean           |

If an invalid heuristic is provided:
```
No such heuristic
Usage:
 e - Euclidean
 m (default) - Manhattan
```
### Example Scenarios
### Case 1: Solvable Puzzle (Manhattan)
#### Input File (`n-puzzle.txt`)
```
1 2 3
4 5 6
7 0 8
```
#### Command
```sh
python main.py m
```
#### Output
```
Solution found in 1 moves:
```
### Case 2: Unsolvable Puzzle
#### Input
```
1 2 3
4 5 6
8 7 0
```
#### Output
```
No solution found.
```
### Time Complexity Analysis
Solving puzzle (`A*`):
	Worst case: $O(b^d)$ (exponential in depth d)
	 Where bb is the branching factor (~4 in this problem)