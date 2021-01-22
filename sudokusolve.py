import numpy as np
import random

sudoku_matrix_try = np.array([[1, 0, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 0, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        ])

#print(sudoku_matrix)
#print(sudoku_matrix.ndim)

def print_sudoku(sudoku_matrix):
    counter_box = 0
    for row in sudoku_matrix:
        print(row)
        for element in row:
            print(element)
            counter_box += 1
            print('')

#print_sudoku(sudoku_matrix)

#print(sudoku_matrix[8, :])

#for idx, x in np.ndenumerate(sudoku_matrix):
#print(idx, x)



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
            if counter%3 == 0:
                strnum += " | "
        if counter_row%3 == 0:
            strnum += "\n ------------------------- \n"
        else:
            strnum += "\n"
    print(strnum)



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
    print(sudoku_matrix)
    print_sudoku(sudoku_matrix)
    return sudoku_matrix

sudoku_text = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"

sudoku_matrix1 = create_table(sudoku_text)

def check_row(matrix, index):
    possible_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for element in matrix[index[0]]:
         possible_nums.discard(element)
    #print(possible_nums)
    return possible_nums

def check_column(matrix, index):
    possible_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for row in range(0,9):
            possible_nums.discard(matrix[row][index[1]])
    #print(possible_nums)
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
    #print(possible_nums)
    return possible_nums

sudoku_matrix = create_table(sudoku_text)

def solve_sudoku(matrix):
    if not find_empty(matrix):
        print_sudoku(matrix)
        return "Solved"
    else:
        index = find_empty(matrix)
    col = check_column(matrix, index)
    square = check_square(matrix, index)
    row = check_row(matrix, index)
    possible_nums = col.intersection(square, row)
    print(len(possible_nums))
    if len(possible_nums) == 1:
        one_el = random.choices(tuple(possible_nums))
        matrix[index[0],index[1]] = one_el[0]
    else:
        one_element = random.choices(tuple(possible_nums))
        possible_nums.discard(one_element[0])
        matrix[index[0], index[1]] = one_element[0]
        return


def find_empty(matrix):
    # finding empty cells with 0 values and get its index
    for idx, row in enumerate(matrix):
        for ind, empty_cell in enumerate(row):
            if empty_cell == 0:
                return [idx, ind]
    return False

# trying to solve it with recursion
def solve_sudoku_rec(matrix):
    for idx, row in enumerate(matrix):
        for ind, element in enumerate(row):
            if element == 0:
                col = check_column(matrix, index=[idx, ind])
                ro = check_row(matrix, index=[idx, ind])
                sq = check_square(matrix, index=[idx, ind])
                possible_nums = col.intersection(sq, ro)
                if len(possible_nums) >= 0:
                    for try_element in possible_nums:
                        matrix[idx, ind] = try_element
                        solve_sudoku_rec(matrix)
                        matrix[idx][ind] = 0
                    return
    print_sudoku(matrix)
    return


solve_sudoku_rec(sudoku_matrix)



#solve_sudoku(sudoku_matrix)


#index = find_empty(sudoku_matrix)
#print(index)

#check_row(sudoku_matrix, index)
#check_column(sudoku_matrix, index)
#check_square(sudoku_matrix, index)
