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

        for i in range(2,100):            #生成非质数容器
            tem = [1,i]
            for j in range(2,i):
                if (i % j == 0):
                    tem.append(j)
            tem.sort(reverse = True)
            if (len(tem) > 2):
                divisition.append(tem)      #为非质数
        
        n = sample(range(51),3)      #将加法加入题目列表
        for i in n:
            tem = [i,'+']
            t = add(i)
            tem.append(t)
            tem.append('=')
            tem.append(i+t)
            timu.append(tem)

        n = sample(divisition,4)    #将除法加入题目列表
        for i in n:
            tem = [i[0],'/']
            t = choice(i[1:-1])     #除数取除自己和1的数，否则太简单了
            tem.append(t)
            tem.append('=')
            tem.append(i[0]//t)
            timu.append(tem)
        
        n = sample(range(1,100),4)  #将减法加入题目列表
        for i in n:
            tem = [i,'-']
            t = sub(i)
            tem.append(t)
            tem.append('=')
            tem.append(i-t)
            timu.append(tem)

        n = sample(range(50),4)   #将乘法加入题目列表
        for i in n:
            tem = [i,'x']
            t = mul(i)
            tem.append(t)
            tem.append('=')
            tem.append(i * t)
            timu.append(tem)

        
    except:
        print("something wrong")