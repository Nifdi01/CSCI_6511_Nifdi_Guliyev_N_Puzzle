import math

def manhattan(n, state):
    distance = 0
    for i in range(n):
        for j in range(n):
            val = state[i][j]
            if val != 0:
                target_i, target_j = (val - 1) // n, (val - 1) % n
                distance += abs((target_i - i) + (target_j - j))
    return distance


def euclidean(n, state):
    distance = 0
    for i in range(n):
        for j in range(n):
            val = state[i][j]
            if val != 0:
                target_i, target_j = (val - 1) // n, (val - 1) % n
                distance += math.sqrt((target_i - i)**2 + (target_j - j)**2)
    return distance