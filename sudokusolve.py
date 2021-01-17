import numpy as np

sudoku_matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]])

print(sudoku_matrix)
print(sudoku_matrix.ndim)

def print_sudoku(sudoku_matrix):
    counter_box = 0
    for row in sudoku_matrix:
        print(row)
        for element in row:
            print(element)
            counter_box += 1
            print('')

#print_sudoku(sudoku_matrix)


def print_sudoku2(sudoku_matrix):
    for three_squares in sudoku_matrix:
        print(three_squares)
        print(", ")

#print_sudoku2(sudoku_matrix)

print(sudoku_matrix[0, :])

#for idx, x in np.ndenumerate(sudoku_matrix):
#print(idx, x)

strnum = ""
counter = 0
counter_row = 0

for sth in range(0,9):
    print(sth)
    counter_row += 1
    if counter_row%3 == 0:
        strnum += "\n"
    for i in sudoku_matrix[sth, :, :]:
        for k in i:
            strnum += str(k)
            counter += 1
            if counter%3 == 0:
                strnum += " "
    print(strnum)



#print(matrix)
#print(matrix.ndim)

def create_table(sudoku_text):
    matrix = np.zeros((9, 3, 3))
    for element in sudoku_text:
        for row_num in range(0,9):
            for row in matrix[row_num, :, :]:
                for number in row:
                    number = number + element
