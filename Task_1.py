#Task_1
class Matrix:
    def __init__(self, matrix_A, matrix_B):
        self.matrix_A = matrix_A
        self.matrix_B = matrix_B

    def print_matrix(self):
        print(f"Matrix A = {self.matrix_A}\nMatrix B = {self.matrix_B}")

    def matrix_add(self):
        if len(self.matrix_A) == len(self.matrix_B) and len(self.matrix_A[0]) == len(self.matrix_B[0]):
            result = [[self.matrix_A[i][j] + self.matrix_B[i][j] for j in range(len(self.matrix_B[0]))]
                      for i in range(len(self.matrix_A))]
            return print(f"A + B = {result}")
        else:
            return print("Matrices of different order cannot be added")

    def matrix_subtract(self):
        if len(self.matrix_A) == len(self.matrix_B) and len(self.matrix_A[0]) == len(self.matrix_B[0]):
            result1 = [[self.matrix_A[i][j] - self.matrix_B[i][j] for j in range(len(self.matrix_A[0]))]
                       for i in range(len(self.matrix_A))]
            result2 = [[self.matrix_B[i][j] - self.matrix_A[i][j] for j in range(len(self.matrix_A[0]))]
                       for i in range(len(self.matrix_A))]
            return print(f"A - B = {result1},\nB - A = {result2}")
        else:
            return print("Matrices of different order cannot be subtracted")

    def matrix_multiply(self):
        if len(self.matrix_A[0]) == len(self.matrix_B):
            result = [[sum(a * b for a, b in zip(self.matrix_A_row, self.matrix_B_col))
                       for self.matrix_B_col in zip(*self.matrix_B)] for self.matrix_A_row in self.matrix_A]
            return print(f"A * B = {result}")
        else:
            return print("If length of rows matrix_A != length of columns matrix_B these matrices cannot be multiply")

    def matrix_mult_num(self, number):
        for i in range(len(self.matrix_A)):
            for j in range(len(self.matrix_A[0])):
                self.matrix_A[i][j] *= number
        return print(f"Matrix_A * {number} = {self.matrix_A}")

    def trans_matrix(self):
        trans_m1 = [[self.matrix_A[j][i] for j in range(len(self.matrix_A))] for i in range(len(self.matrix_A[0]))]
        trans_m2 = [[self.matrix_B[j][i] for j in range(len(self.matrix_B))] for i in range(len(self.matrix_B[0]))]
        return print(f"Matrix_A_trans = {trans_m1}\nMatrix_B_trans = {trans_m2}")




m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]])
m.print_matrix()
m.trans_matrix()
m.matrix_add()
m.matrix_subtract()
m.matrix_multiply()
m.matrix_mult_num(3)
