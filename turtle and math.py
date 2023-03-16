from random import *
import turtle
#coding = UTF-8


def add(n):             #加法题的辅助函数,生成被加数
    return choice(range(100-n))

def sub(n):             #减法题的辅助函数，生成减数
    return choice(range(n+1))

def mul(n):             #乘法题的辅助函数，生成乘数
    return choice(range(100//n+1))

def write_square():    #画方框
    turtle.setheading(0)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)

def move_turtle(turtle, x, y):      #无痕移动
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def write_question(turtle, question, x, y):   #写问题部分
    move_turtle(turtle, x, y)
    turtle.write(question, font=("Arial", 16, "normal"))
    move_turtle(turtle, x+100, y)
    write_square()

def write_answer(turtle, answer, x, y):    #写答案部分
    move_turtle(turtle, x, y)
    turtle.write(answer, font=("Arial", 16, "normal"))

def write_title(turtle, title, x, y):      #写标题部分
    move_turtle(turtle, x, y)
    turtle.write(title, font=("Arial", 16, "normal"))
    move_turtle(turtle,x + 10, y)
    turtle.setheading(0)
    turtle.forward(600)                     #画横线

def create_paper(timu,num_questions_per_row=3, num_rows=5, paper_width=0.99, paper_height=0.99):
    turtle.setup(paper_width, paper_height)               #准备部分
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    
    write_title(turtle, "Quiz", -600, 300)                 #问题部分
    for i in range(num_rows):
        for j in range(num_questions_per_row):
            question = ' '.join(timu[(3 * i + j)][0:4])
            x = -550 + j * 200                             #控制题目的间隔
            y = 260 + i * -50
            write_question(turtle, question, x, y)

    write_title(turtle, "Answer", -600, 30)                 #答案部分
    for i in range(num_rows):
        for j in range(num_questions_per_row):
            question = ' '.join(timu[(3 * i + j)][0:4])
            answer = str(timu[(3 * i + j)][4])
            x = -550 + j * 200
            y = -10 + i * -50
            write_question(turtle, question, x, y)
            write_answer(turtle, answer, x + 105, y)
    
    turtle.exitonclick()

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
            tem = [str(i),'+']
            t = add(i)
            tem.append(str(t))          #将数字转化为字符串，方便之后海龟画图的整合
            tem.append('=')
            tem.append(str(i+t))
            timu.append(tem)

        n = sample(divisition,4)    #将除法加入题目列表
        for i in n:
            tem = [str(i[0]),'/']
            t = choice(i[1:-1])     #除数取除自己和1的数，否则太简单了
            tem.append(str(t))
            tem.append('=')
            tem.append(str(i[0]//t))
            timu.append(tem)
        
        n = sample(range(1,100),4)  #将减法加入题目列表
        for i in n:
            tem = [str(i),'-']
            t = sub(i)
            tem.append(str(t))
            tem.append('=')
            tem.append(str(i-t))
            timu.append(tem)

        n = sample(range(50),4)   #将乘法加入题目列表
        for i in n:
            tem = [str(i),'x']
            t = mul(i)
            tem.append(str(t))
            tem.append('=')
            tem.append(str(i * t))
            timu.append(tem)

        shuffle(timu)          #题目乱序
        create_paper(timu)      #生成卷子
    except:
        print("something wrong")