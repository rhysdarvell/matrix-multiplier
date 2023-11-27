import csv

def main():
    print("hello world")

    # matrix1 = [[1, 2],
    #            [3, 4],
    #            [5, 6]]

    matrix1 = []
    matrix2 = []
    
    # matrix2 = [[7, 8, 9],
    #            [10,11,12]]
    
    with open('matrix1.csv') as matrix1reader:
        read = csv.reader(matrix1reader, delimiter=',')

        for row in read:
            int_row = []
            for item in row:
                int_row.append(int(item))
            matrix1.append(int_row)

    with open('matrix2.csv') as matrix2reader:
        read = csv.reader(matrix2reader, delimiter=',')

        for row in read:
            int_row = []
            for item in row:
                int_row.append(int(item))
            matrix2.append(int_row)


    print(matrix1)
    print(matrix2)


    
    #print(multiply_matrix(matrix1, matrix2))

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