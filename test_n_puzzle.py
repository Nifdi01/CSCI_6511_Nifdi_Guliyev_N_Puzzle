import unittest
import tempfile
import os
from utils import generate_goal_state, find_blank, read_puzzle
from n_puzzle import NPuzzle

class TestUtils(unittest.TestCase):
    def test_generate_goal_state(self):
        """
        Test that the generate_goal_state function produces the correct goal state
        for a 3x3 puzzle.
        """
        expected_goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 0)
        )
        goal_state = generate_goal_state(3)
        self.assertEqual(goal_state, expected_goal)

    def test_find_blank(self):
        """
        Test that find_blank correctly identifies the blank tile (0) in a puzzle state.
        """
        state = (
            (1, 2, 3),
            (4, 0, 6),
            (7, 8, 5)
        )
        blank_position = find_blank(state, 3)
        self.assertEqual(blank_position, (1, 1))

    def test_read_puzzle(self):
        """
        Test that read_puzzle correctly reads a puzzle from a temporary file.
        The file contains a 3x3 puzzle with each row having the correct number of elements.
        """
        # Define puzzle content with three rows of three numbers each.
        puzzle_content = "1\t2\t3\n4\t5\t6\n7\t8\t0\n"
        # Create a temporary file and write the puzzle content to it.
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_file:
            tmp_file.write(puzzle_content)
            tmp_file_path = tmp_file.name
        try:
            puzzle = read_puzzle(tmp_file_path)
            expected_puzzle = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ]
            self.assertEqual(puzzle, expected_puzzle)
        finally:
            os.remove(tmp_file_path)


class TestNPuzzleSolver(unittest.TestCase):
    def test_invalid_npuzzle(self):
        """
        Test that initializing NPuzzle with an invalid configuration (rows of unequal length)
        raises a ValueError.
        """
        # Row 2 is missing an element.
        invalid_state = [
            [1, 2, 3],
            [4, 5],
            [7, 8, 0]
        ]
        with self.assertRaises(ValueError):
            NPuzzle(invalid_state, heuristic="m")

    def test_get_neighbors(self):
        """
        Test that get_neighbors produces the correct number of neighbors for a 2x2 puzzle.
        For a blank in the top-left corner, only moves to the right and down are possible.
        """
        initial_state = (
            (0, 1),
            (2, 3)
        )
        # Create NPuzzle instance from a list-of-lists (constructor converts it to a tuple-of-tuples)
        puzzle = NPuzzle([list(row) for row in initial_state], heuristic="m")
        neighbors = puzzle.get_neighbors(initial_state)
        # For blank at top-left in a 2x2 puzzle, expect 2 neighbors.
        self.assertEqual(len(neighbors), 2)
        # Validate that the blank moves to an expected position.
        expected_positions = [(0, 1), (1, 0)]
        blank_positions = [find_blank(state, 2) for state in neighbors]
        for pos in blank_positions:
            self.assertIn(pos, expected_positions)

    def test_solve_already_solved(self):
        """
        Test that the solver returns 0 moves when the puzzle is already solved.
        """
        # Generate the goal state for a 3x3 puzzle.
        initial_state = generate_goal_state(3)
        # Convert immutable goal state to list-of-lists for NPuzzle constructor.
        initial_state_list = [list(row) for row in initial_state]
        puzzle = NPuzzle(initial_state_list, heuristic="m")
        moves = puzzle.solve()
        self.assertEqual(moves, 0)

    def test_solve_one_move(self):
        """
        Test that the solver finds the solution in 1 move for a 2x2 puzzle that is one move away from the goal.
        For a 2x2 puzzle, the goal state is ((1,2), (3,0)).
        """
        # One move away: blank (0) is swapped with 3.
        initial_state = [
            [1, 2],
            [0, 3]
        ]
        puzzle = NPuzzle(initial_state, heuristic="m")
        moves = puzzle.solve()
        self.assertEqual(moves, 1)

    def test_solve_5x5_one_move(self):
        """
        Test that the solver finds the solution in 1 move for a 5x5 puzzle that is one move away from the goal.
        The goal state for a 5x5 puzzle has the blank (0) at the bottom-right; swapping it with its left neighbor 
        results in a puzzle that is one move away.
        """
        # Generate the goal state for a 5x5 puzzle.
        solved = generate_goal_state(5)
        puzzle_list = [list(row) for row in solved]
        # Swap the blank (0) with its left neighbor in the last row.
        puzzle_list[4][3], puzzle_list[4][4] = puzzle_list[4][4], puzzle_list[4][3]
        puzzle = NPuzzle(puzzle_list, heuristic="m")
        moves = puzzle.solve()
        self.assertEqual(moves, 1)

    def test_solve_6x6_one_move(self):
        """
        Test that the solver finds the solution in 1 move for a 6x6 puzzle that is one move away from the goal.
        The goal state for a 6x6 puzzle has the blank (0) at the bottom-right; swapping it with its left neighbor 
        results in a puzzle that is one move away.
        """
        # Generate the goal state for a 6x6 puzzle.
        solved = generate_goal_state(6)
        puzzle_list = [list(row) for row in solved]
        # Swap the blank (0) with its left neighbor in the last row.
        puzzle_list[5][4], puzzle_list[5][5] = puzzle_list[5][5], puzzle_list[5][4]
        puzzle = NPuzzle(puzzle_list, heuristic="m")
        moves = puzzle.solve()
        self.assertEqual(moves, 1)

if __name__ == '__main__':
    unittest.main()
