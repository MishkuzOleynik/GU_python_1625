class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self, in_matrix = None):
        in_list = in_matrix if in_matrix else self.matrix
        # print (in_list)
        str_matrix = ''
        for item in in_list:
            str_matrix += ''.join(str(item)) + '\n'
        return str_matrix


    def __add__(self, other):
        result = []
        for i, el in enumerate(self.matrix):
            if len(self.matrix) != len(other.matrix) or len(el) != len(other.matrix[i]):
                print('Сложение матриц разных размерностей невозможно')
                exit()
            else:
                result.append([v + other.matrix[i][k] for k, v in enumerate(el)])
        return self.__str__(result if result != [] else None)




matrix_a = Matrix([[10, 15, 82],
            [23, 34, 89],
            [92, 17, 41]])

matrix_b = Matrix([[17, 2, 63],
            [45, 16, 13],
            [43, 72, 99]])

matrix_c = Matrix([[17, 2, 63, 65],
            [45, 16, 13, 51],
            [43, 72, 99, 90]])

print(matrix_a)
print(matrix_b)
print(matrix_c)
matrix_d = matrix_a + matrix_b
print(matrix_d)