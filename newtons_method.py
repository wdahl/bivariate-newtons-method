import math

def f(x, y):
    return math.pow(x, 2) + x*math.pow(y, 3) - 9

def div_fx(x,y):
    return 2*x + math.pow(y,3)

def div_fy(x,y):
    return 3*x*math.pow(y,2)

def g(x, y):
    return 3*math.pow(x, 2)*y - math.pow(y, 3) - 4

def div_gx(x,y):
    return 6*x*y

def div_gy(x,y):
    return 3*math.pow(x,2) - 3*math.pow(y,2)

def det(x, y):
    return 6*math.pow(x,3) - 6*x*math.pow(y,2) - 15*math.pow(x,2)*math.pow(y,3) - 3*math.pow(y,5)

def inv(x,y,j):
    det_reciprical = 1/det(x,y)
    new_j = [[0,0],
             [0,0]]
    
    new_j[0][0] = j[1][1]
    new_j[0][1] = 0 - j[0][1]
    new_j[1][0] = 0 - j[1][0]
    new_j[1][1] = j[0][0]

    for i in range(0, 2):
        for k in range(0, 2):
            new_j[i][k] *= det_reciprical

    return new_j

def matrix_mul(v, j):
    vector = []
    for i in range(0, 2):
        sum = 0
        for k in range(0, 2):
            sum += j[i][k] * v[k]

        vector.append(sum)

    return vector

def vector_sub(v1, v2):
    v3 = [0,0]
    for i in range(0, 2):
        v3[i] = v1[i]-v2[i]

    return v3

x0 = [2.98, 0.15]
error = [1, 1]
count = 1

while abs(error[0]) > math.pow(10,-12) or abs(error[1]) > math.pow(10, -12):
    J = [[div_fx(x0[0],x0[1]), div_fy(x0[0],x0[1])],
         [div_gx(x0[0],x0[1]), div_gy(x0[0],x0[1])]]

    F = [f(x0[0], x0[1]), g(x0[0], x0[1])]

    x1 = vector_sub(x0, matrix_mul(F, inv(x0[0], x0[1], J)))

    error = vector_sub(x1, x0)

    print(f'Iteration {count}:')
    print(f'x0 = {x0}')
    print(f'x1 = {x1}')
    print(f'error = {error}')

    count += 1
    x0 = x1