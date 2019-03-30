import numpy as np


def dot(v1, v2, length):

    product = 0

    for i in range(0, length):
        product = product + v1[i] * v2[i]

    # return sum(x*y for x, y in zip(v1, v2))
    # this also works and doesn't require length

    return product


def cross(v3, v4, crossP):

    crossP.append(v3[1] * v4[2] - v3[2] * v4[1])
    crossP.append(v3[2] * v4[0] - v3[0] * v4[2])
    crossP.append(v3[0] * v4[1] - v3[1] * v4[0])

    return crossP


v_1 = [0, 0, 1]  # [0, 0, 1]  # [1, 2, 3]
v_2 = [1, 0, 0]  # [1, 0, 0] # [4, 5, 6]
cross_P = []
n = 3

print("Dot product: ", dot(v_1, v_2, n))
print("Numpy dot product :", np.dot(v_1, v_2))
print("Cross product: ", cross(v_1, v_2, cross_P))
print("Numpy cross product :", np.cross(v_1, v_2))
