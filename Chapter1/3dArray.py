
def get_rows_from_user():
    """This function just gets three rows from the user and returns them in a list
    for example: [[1,2,3], [4,5,6], [7,8,9]]
    """
    matrix = []
    for i in range(3):
        try:
            row = list(map(int,input(f"Please enter numbers of row number \n"
                                     f"{i + 1} and separate them with one space \n"
                                     f"(for example  1 2 3) : ").split(' ')))
            matrix.append(row)
        except ValueError:
            print("Just please enter a numerical value")
            continue
    return matrix

def calculate_row_sums(matrix):
    """This function calculates the row sums"""
    print("Row sums:")
    for i in range(3):
        row_sum = sum(matrix[i])
        print(f"Row {i + 1}: {row_sum}")

def calculate_column_sums(matrix):
    """This function calculates the column sums"""
    print("Column sums:")
    for j in range(3):
        col_sum = 0
        for i in range(3):
            col_sum += matrix[i][j]
        print(f"Column {j + 1}: {col_sum}")

def main():
    matrix = get_rows_from_user()
    calculate_row_sums(matrix)
    calculate_column_sums(matrix)

if __name__ == "__main__":
    main()