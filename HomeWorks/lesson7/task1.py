# Add task1.py

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
    def __add__(self):
        mat_list = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                mat_list[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat_list]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat_list]))

new_matrix = Matrix([[9, 24, 15],
                    [10, 21, 27],
                    [45, 54, 13]],
                   [[49, 12, 7],
                    [11, 15, 99],
                    [27, 9, 107]])

print(new_matrix.__add__())