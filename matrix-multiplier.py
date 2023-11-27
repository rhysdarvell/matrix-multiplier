import csv
import time

def main():
    file1 = 'matrix1.csv'
    file2 = 'matrix2.csv'

    matrix1 = []
    matrix2 = []
    
    with open(file1) as matrix1reader:
        read = csv.reader(matrix1reader, delimiter=',')

        for row in read:
            int_row = []
            for item in row:
                int_row.append(int(item))
            matrix1.append(int_row)

    with open(file2) as matrix2reader:
        read = csv.reader(matrix2reader, delimiter=',')

        for row in read:
            int_row = []
            for item in row:
                int_row.append(int(item))
            matrix2.append(int_row)


    # print(matrix1)
    # print(matrix2)


    start_time = time.time_ns()
    print(multiply_matrix(matrix1, matrix2))
    end_time = time.time_ns()
    print(end_time - start_time)

#calculates one cell of the result matrix
def multiply_cell(x, y, matrix1, matrix2):
    total = 0

    for i in range(len(matrix2)):
        total += matrix1[y][i] * matrix2[i][x]

    return total

def multiply_matrix(matrix1, matrix2):
    width = len(matrix2[0])
    height = len(matrix1)
    result = [[0 for i in range(width)] for i in range(height)]

    for i in range(height):
        for j in range(width):
            result[i][j] = multiply_cell(j, i, matrix1, matrix2)

    return result

if __name__ == "__main__":
    main()