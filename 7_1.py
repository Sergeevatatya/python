class Matrix:
    def __init__(self, mat1, mat2):
        self.mat1 = mat1
        self.mat2 = mat2
    def __add__(self):
        res = [[0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.mat1)):
            for j in range(len(self.mat2[i])):
                res[i][j] = self.mat1[i][j] + self.mat2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in res]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in res]))
my_matrix = Matrix([[55, 1, 15],
                    [10, 17, 56]],
                   [[75, 25, 2],
                    [9, 85, 63]])
print(my_matrix.__add__())
