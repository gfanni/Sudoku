import numpy as np

sudoku_matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
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

# create_table(sudoku_text)

def check_row(element):

def check_column(element):

def check_square(element):

def solve_sudoku(sudoku_text):
    sudoku_matrix = create_table(sudoku_text)


