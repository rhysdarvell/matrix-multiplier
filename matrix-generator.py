import random
import csv

def main():

    matrix = []

    width = 1000
    height = 1000

    output_file = "matrix.csv"

    for i in range(width):
        row = []

        for j in range(height):
            random_number = random.randint(0, 100)
            row.append(random_number) #TODO change to random number

        matrix.append(row)

    #print(matrix)

    file = open(output_file, 'w+')
    
    with file:
        write = csv.writer(file)
        write.writerows(matrix)

    
        


    print("hello")


if __name__ == "__main__":
    main()