import unittest
from source import sudoku_solver

class MyTestCase(unittest.TestCase):
    def test_find_next_empty(self):
        next_empty_index = [-1, -1]
        grid = [[2, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 3, 0, 0],
                [1, 4, 1, 0d, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 8, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 6, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 3, 0, 0, 0]]
        has_empty = sudoku_solver.find_next_empty(grid, next_empty_index)
        self.assertEqual(has_empty, True, "Test: 0,1 returned")
        self.assertEqual(next_empty_index, [0, 1], "Test: 0,1 is empty")


        grid = [[2, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 4, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0]]
        has_empty = sudoku_solver.find_next_empty(grid, next_empty_index)
        self.assertEqual(next_empty_index, [8, 8], "Test: 8,8 found")
        self.assertEqual(has_empty, True, "Test: 8,8 empty")

        grid = [[2, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 4, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        has_empty = sudoku_solver.find_next_empty(grid, next_empty_index)
        self.assertEqual(has_empty, False, "Test: Full Grid")

    def test_candidate_digit_checker(self):
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 1, 0, 4), True, "Is-Valid Case 1")

        grid = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 6]]
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 0, 4), False, "Is-Valid Case 2")

        grid = [[4, 0, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 6]]
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 1), False, "Is-Valid Case 3-1")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 2), False, "Is-Valid Case 3-2")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 3), True, "Is-Valid Case 3-3")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 4), False, "Is-Valid Case 3-4")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 5), False, "Is-Valid Case 3-5")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 6), False, "Is-Valid Case 3-6")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 7), False, "Is-Valid Case 3-7")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 8), False, "Is-Valid Case 3-8")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 9), False, "Is-Valid Case 3-9")

        grid = [[4, 0, 5, 0, 0, 0, 0, 0, 0],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 0, 6, 1, 9, 5, 3, 4, 7],
                [3, 0, 4, 6, 8, 2, 9, 1, 5],
                [9, 0, 1, 7, 4, 3, 6, 2, 8],
                [5, 0, 9, 3, 2, 6, 8, 7, 4],
                [2, 0, 8, 9, 5, 7, 1, 3, 6],
                [7, 0, 3, 4, 1, 8, 2, 5, 6]]
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 1), False, "Is-Valid Case 4-1")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 2), False, "Is-Valid Case 4-2")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 3), True, "Is-Valid Case 4-3")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 4), False, "Is-Valid Case 4-4")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 5), False, "Is-Valid Case 4-5")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 6), False, "Is-Valid Case 4-6")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 7), False, "Is-Valid Case 4-7")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 8), False, "Is-Valid Case 4-8")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 9), False, "Is-Valid Case 4-9")

        grid = [[4, 0, 5, 2, 6, 9, 7, 8, 1],
                [0, 8, 0, 5, 7, 1, 4, 9, 3],
                [0, 9, 0, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 6]]
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 1), False, "Is-Valid Case 5-1")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 2), False, "Is-Valid Case 5-2")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 3), True, "Is-Valid Case 5-3")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 4), False, "Is-Valid Case 5-4")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 5), False, "Is-Valid Case 5-5")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 6), False, "Is-Valid Case 5-6")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 7), False, "Is-Valid Case 5-7")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 8), False, "Is-Valid Case 5-8")
        self.assertEqual(sudoku_solver.check_if_num_valid_at_locn(grid, 0, 1, 9), False, "Is-Valid Case 5-9")


    def test_solve_puzzle(self):
        #Test the full solution engine
        grid = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 0, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 6]]
       # res = sudoku_solver.solve_puzzle(grid)
       # self.assertEqual(res, False, "Solve single-variable puzzle")

        grid = [[4, 0, 5, 2, 6, 9, 7, 8, 1],
                [0, 8, 0, 5, 7, 1, 4, 9, 3],
                [0, 9, 0, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 0, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 6]]
       # res = sudoku_solver.solve_puzzle(grid)
       # self.assertEqual(res, True, "Solve several-variable puzzle")

        grid = [
            [8, 7, 1, 2, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 6, 0, 1, 7, 0],
            [0, 0, 0, 1, 3, 0, 0, 0, 8],
            [0, 2, 0, 0, 8, 9, 4, 0, 0],
            [3, 0, 8, 0, 0, 0, 5, 0, 6],
            [0, 0, 9, 5, 1, 0, 0, 2, 0],
            [5, 0, 0, 0, 4, 6, 0, 0, 0],
            [0, 8, 6, 0, 7, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 2, 6, 4, 9]
        ]
        res = sudoku_solver.solve_puzzle(grid)
        self.assertEqual(res, True, "Solve Full Puzzle")

        grid = [[4, 0, 5, 2, 6, 9, 7, 8, 1],
                [0, 8, 0, 5, 7, 1, 4, 9, 3],
                [0, 9, 0, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 2, 0, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 9, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 6]]
        res = sudoku_solver.solve_puzzle(grid)
        self.assertEqual(res, False, "Solve invalid puzzle")




if __name__ == '__main__':
    unittest.main()
