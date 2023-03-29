import numpy
import math
def get_max_row_in_column(matrix_a, j,n):   #获取第j列最大的数所在行
    max_item = abs(matrix_a[j][j])
    max_row = j
    for i in range(j,n):
        if abs(matrix_a[i][j]) > abs(max_item):
            max_item = matrix_a[i][j]
            max_row = i
    return max_row


def gaosi(a,b,n):
    print("gaosi:")
    x = []
    for k in range(n-1):
        m = [0]*(k+1)
        a_tem = []
        b_tem = []
        for i in range(n-k):
            m.append(a[k][i][k]/a[k][k][k])
            a_tem2 = []
            for j in range(n-k):   
                a_tem2.append(a[k][i][j] - m[i]*a[k][k][j])
            a_tem.append(a_tem2)
            b_tem.append(b[k][i] - m[i]*b[k][k])   
        a.append(a_tem)
        b.append(b_tem)
    x_n = b[n-1][0]/a[n-1][0][0]
    x.append(x_n)
    for i in range(n-2,-1,-1):
        x_i = (b[i][0]-sum(a[i][0][j]* x[j-1] for j in range(1,n-i)))/(a[i][0][0])
        x.append(x_i)
    x.reverse
    print(x)

def liezhu(a,b,n):
    print("liezhuxiaoyuanfa:")
    a = [[14,2,1,5],
        [8,17,2,10],
        [4,18,3,6],
        [12,26,11,20]]
    b = [11,12,13,14]
    n = 4
    xigema = 0.000001
    for k in range(0,n-1):
        i_k = get_max_row_in_column(a,k,n)
        if abs(a[i_k][i_k]) < xigema:
            print("det a = 0")
            exit(0)
        else:
            if i_k == k:
                pass
            else:
                a[i_k],a[k] = a[k],a[i_k]
            for i in range(k+1,n):
                a_ik = a[i][k]/a[k][k]
                for j in range(k+1,n):
                    a[i][j] = a[i][j] - a_ik *a[k][j]
                    b[i] = b[i] - a_ik * b[k]
    if abs(a[n-1][n-1]) < xigema:
        print("det a = 0")
        exit(0)
    else:
        b[n-1] = b[n-1] / a[n-1][n-1]
        for i in range(n-2,-1,-1):
            b[i] = (b[i] - sum(a[i][j] * b[j] for j in range(i+1,n)))/a[i][i]
    print(b)
def jocobi():
    print("jocobi:")
    a = [[14,2,1,5],
        [8,17,2,10],
        [4,18,3,6],
        [12,26,11,20]]
    b = [11,12,13,14]
    x = [-1,-1,-1,5]
    n = 4
    N = 100
    xigema = 0.001
    for k in range(N):
        y = []
        for i in range(n):
            y.append((b[i] - sum(a[i][j] * x[j] for j in range(n) if j != i))/a[i][i])
        e = max(abs(y[i]-x[i]) for i in range(n))
        if (e < xigema):
            print(y)
            exit(0)
        else:
            x = y    
    print("defate")

def gussseidel():
    print("gussseidel:")
    a = [[14,2,1,5],
        [8,17,2,10],
        [4,18,3,6],
        [12,26,11,20]]
    b = [11,12,13,14]
    x = [-1,-1,-1,5]
    n = 4
    N = 10000
    xigema = 0.001
    for k in range(N):
        e = 0
        for i in range(n):
            t = x[i]
            x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(n) if j != i))/a[i][i]
            if (abs(x[i] - t) <= e):
                pass
            else:
                e = abs(x[i] - t)
        if e < xigema:
            print(k)
            print(x)
            exit(0)
    print("defate with",N,"times")
if __name__  == '__main__':
    a = [[[14,2,1,5],[8,17,2,10],[4,18,3,6],[12,26,11,20]]]
    b = [[11,12,13,14]]
    n = 4
    gaosi(a,b,n)
    liezhu(a,b,n)
    jocobi()
    gussseidel()
    




    
