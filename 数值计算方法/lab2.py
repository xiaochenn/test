import numpy
import math

if __name__  == '__main__':
    print("高斯法：")
    a = [[[14,2,1,5],[8,17,2,10],[4,18,3,6],[12,26,11,20]]]
    b = [[11,12,13,14]]
    x = []
    n = 4
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
    
