from random import *
#coding = UTF-8


def add(n):             #加法题的辅助函数,生成被加数
    return choice(range(0,100,1))

def sub(n):             #减法题的辅助函数，生成减数
    return choice(range(0,n+1,1))

def mul(n):             #乘法题的辅助函数，生成乘数
    return choice(range(0,100//n+1,1))

def ifPrime(n):
   pass 
    

if __name__ == '__main__':
    try:
        timu = []
        divisition = []
        timu.append(1)
        timu.append(None)
        print(timu)
    except:
        pass