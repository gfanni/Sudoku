import numpy as np


# visualize the sudoku table
def print_sudoku(sudoku_matrix):
    strnum = ""
    counter = 0
    counter_row = 0
    for row in sudoku_matrix:
        counter_row += 1
        for element in row:
            strnum += str(int(element))
            strnum += " "
            counter += 1
            if counter % 3 == 0:
                strnum += " | "
        if counter_row % 3 == 0:
            strnum += "\n-------------------------- \n"
        else:
            strnum += "\n"
    print(strnum)


# convert SDM format into a 2D matrix
def create_table(sudoku_text):
    sudoku_matrix = np.zeros((9, 9))
    x = 0
    y = 0
    for number in sudoku_text:
        sudoku_matrix[y, x] = int(number)
        x += 1
        if x > 8:
            y += 1
            x = 0
    print_sudoku(sudoku_matrix)
    return sudoku_matrix


# find the numbers that could be correct according to the rules (row, column and square)
def check_row(matrix, index):
    possible_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for element in matrix[index[0]]:
        possible_nums.discard(element)
    return possible_nums


def check_column(matrix, index):
    possible_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for row in range(0, 9):
        possible_nums.discard(matrix[row][index[1]])
    return possible_nums


def check_square(matrix, index):
    possible_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    box_len = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    row = -1
    column = -1
    for box_side in box_len:
        if index[0] in box_side:
            row = box_side
        if index[1] in box_side:
            column = box_side
    for side in row:
        for idx in column:
            possible_nums.discard(matrix[side][idx])
    return possible_nums


# return the SDM format of the sudoku matrix
def sudoku_sdm(matrix):
    sdm_string = ""
    for row in matrix:
        for element in row:
            sdm_string = sdm_string + str(int(element))
    return sdm_string


# solve the sudoku with recursion, return the solution in SDM format
def solve_sudoku_rec(matrix):
    for idx, row in enumerate(matrix):
        for ind, element in enumerate(row):
            if element == 0:  # if the matrix element is 0, we check which numbers can be written in that position
                col = check_column(matrix, index=[idx, ind])
                ro = check_row(matrix, index=[idx, ind])
                sq = check_square(matrix, index=[idx, ind])
                possible_nums = col.intersection(sq, ro)  # these are the numbers that can be used

                # if we have 0 elements in the possible_nums set, it means we filled one of the empty spaces with an
                # incorrect number so we should return
                if len(possible_nums) >= 0:  # here's where the magic happens
                    for try_element in possible_nums:
                        # we try to solve the sudoku with one of the numbers of the possible_nums set
                        matrix[idx, ind] = try_element

                        # we call this function again with the new matrix and continue filling
                        solve_sudoku_rec(matrix)

                        # if we returned in one of the functions before checking all empty fields, set that number
                        # again to 0 - and we can go back until where the incorrect number was chosen and try it with
                        # another possible number
                        matrix[idx][ind] = 0
                    return

    print_sudoku(matrix)
    sdm = sudoku_sdm(matrix)

    # we return when when we checked all empty spaces and could fill it with the possible number
    return sdm

sudoku_text = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"

# infinite loop bc endless solutions - need to handle that somehow!
sudoku_text2 = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"

sudoku_matrix = create_table(sudoku_text)
output_sdm = solve_sudoku_rec(sudoku_matrix)
