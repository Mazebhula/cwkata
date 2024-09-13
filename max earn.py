import numPy as np

def count_different_matrices(matrices):
    size = len(matrices)
    new = []
    rotated = []
    count = 0
    for item in matrices:
        new = [item[2],item[0],item[3],item[1]]
        rotated.append(new)
    for item in matrices:
        for items in rotated:
            if np.array_equal(item , new):
                count+=1
        print(count)
        

matrices = [[1, 2, 3, 4],
            [3, 1, 4, 2],
            [4, 3, 2, 1],
            [2, 4, 1, 3]]

count_different_matrices(matrices)