from random import *
#coding = UTF-8


def add(n):             #加法题的辅助函数,生成被加数
    return choice(range(100-n))

def sub(n):             #减法题的辅助函数，生成减数
    return choice(range(n+1))

def mul(n):             #乘法题的辅助函数，生成乘数
    return choice(range(100//n+1))

    

if __name__ == '__main__':
    try:
        timu = []
        divisition = []
        prime = []          #质数容器

        for i in range(2,100):            #生成非质数容器和非质数容器
            tem = [1,i]
            for j in range(2,i):
                if (i % j == 0):
                    tem.append(j)
            tem.sort(reverse = True)
            if (len(tem) > 2):
                divisition.append(tem)      #为非质数
            else:
                prime.append(i)         #为质数
        
        n = sample(range(100),4)
        for i in n:
            tem = [i,'+']
            t = add(i)
            tem.append(t)
            print(tem)
    except:
        print("something wrong")