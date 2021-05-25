def validate_grid(puzzle):
    """
    Verify if an input grid is a legal puzzle
    :param puzzle:
    :return:
    """
    # Verify input Types: Must be a 9x9 list
    # Verify inputs: Puzzle must contain only digits


def solve_puzzle(puzzle):
    if not is_valid_puzzle(puzzle):
        return False

    return solve_puzzle_iter(puzzle)



def solve_puzzle_iter(puzzle):
    """
    Take in a partially filled sudoku puzzle, and use a backtracking
    algorithm to fill the puzzle
    :param puzzle: [9][9] list of integer digits, 1-9
    :return: true if the puzzle is solved, false if the puzzle is unsolvable

    """
    # Base case - if all locations are filled, return true
    # Guarded return, directly
    try:
        next_empty_index = [0, 0]
        if not find_next_empty(puzzle, next_empty_index):
            print("Solved Puzzle")
            print_grid(puzzle)
            return True

        working_row = next_empty_index[0]
        working_col = next_empty_index[1]
        for candidate_digit in range(1, 10):
            if check_if_num_valid_at_locn(puzzle,
                                          working_row,
                                          working_col,
                                          candidate_digit):
                puzzle[working_row][working_col] = candidate_digit

                if(solve_puzzle_iter(puzzle)):
                    return True

                # If there are no valid solutions from here, undo it
                puzzle[working_row][working_col] = 0

        # If all candidates have failed, backtrack another step
        return False
    except Exception as e:
        print(e)
        return False

def print_grid(puzzle):
    """
    Consume a puzzle, dump it to the console
    :param puzzle:
    :return: string representation of a sudo puzzle
    """
    out = ""
    for i_row in range(9):
        for i_col in range(9):
            out += str(puzzle[i_row][i_col])
            if i_col != 8:
                out += "|"
        out += "\n"
        #if i_row != 8:
        #out += "\n"
    print(out)


def find_next_empty(puzzle, indx):
    """
    Find the next un-filled slot in a supplied puzzle
    Integer values of 0 will be considered empty
    :param puzzle: [9][9] grid of integer, 0-9
    :param indx: reference to row/col of next empty entry
    :return: true if there's another empty, false else
    """
    for i_row in range(9):
        for i_col in range(9):
            if puzzle[i_row][i_col] == 0:
                indx[0] = i_row
                indx[1] = i_col
                return True
    return False


def is_valid_puzzle(puzzle):
    for i_row in range(9):
        for i_col in range(9):
            chk_digit = puzzle[i_row][i_col]
            if chk_digit != 0:
                puzzle[i_row][i_col] = 0
                if not check_if_num_valid_at_locn(puzzle, i_row, i_col, chk_digit):
                    print("Invalid Puzzle")
                    return False
                puzzle[i_row][i_col] = chk_digit
    return True


def check_if_num_valid_at_locn(puzzle, i_row, i_col, digit):
    """
    Check if a given digit will break a sudoku puzzle
    :param puzzle:
    :param i_row:
    :param i_col:
    :param digit:
    :return:
    """
    # Check if it occurs in the row
    if digit in puzzle[i_row]:
        return False
    # Check if it's in the column
    for i in range(9):
        if(puzzle[i][i_col] == digit):
            return False
    # Check if it's used in the local 3x3 box
    #   Boxes: 0,0 to 2,2   3,0 to 5,2  6,0 to 8,2
    #          0,3 to 2,5   3,3 to 5,5  6,3 to 8,5
    #          0,6 to 2,8   3,6 to 5,8  6,6 to 8,8
    box_start_row = (i_row - (i_row % 3))
    box_start_col = (i_col - (i_col % 3))
    for i in range(box_start_row, box_start_col + 3):
        for j in range(box_start_col, box_start_row + 3):
            if puzzle[i][j] == digit:
                return False
    # If we make it here, it's legal
    return True


if __name__ == "__main__":
    """
    Launch the program, if given a main function
    """
    print("This is a solver")
