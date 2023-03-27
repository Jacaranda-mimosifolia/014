import math
import random
from collections import deque
from turtle import *

colormode(255)
setup(1000, 1100, 700, 0)
# screensize(1000, 1100)
bgcolor(25, 25, 112)
# tracer(False)


def move1():  # 云彩
    for I in range(6):
        if I == 0:
            a = random.randint(100, 105)
            t1.color(12, 12, 60)
            t1.pensize(100)
            t1.pu()
            t1.setx(-500)
            t1.sety(15 * math.sin(-500 / 60) + 530 - a)
            t1.pd()
            for i in range(-500, 500):
                t1.setx(i)
                t1.sety(15 * math.sin(i / 60) + 530 - a)
        elif I == 1:
            a = random.randint(250, 255)
            t1.color(8, 8, 64)
            t1.pensize(96)
            t1.pu()
            t1.setx(-500)
            t1.sety(15.5 * math.sin(-500 / 59) + 530 - a)
            t1.pd()
            for i in range(-500, 500):
                t1.setx(i)
                t1.sety(16 * math.sin(i / 59) + 530 - a)
        elif I == 2:
            a = random.randint(392, 397)
            t1.color(5, 5, 69)
            t1.pensize(92)
            t1.pu()
            t1.setx(-500)
            t1.sety(16 * math.sin(-500 / 58) + 530 - a)
            t1.pd()
            for i in range(-500, 500):
                t1.setx(i)
                t1.sety(17 * math.sin(i / 58) + 530 - a)
        elif I == 3:
            a = random.randint(528, 533)
            t1.color(3, 3, 75)
            t1.pensize(88)
            t1.pu()
            t1.setx(-500)
            t1.sety(16.5 * math.sin(-500 / 57) + 530 - a)
            t1.pd()
            for i in range(-500, 500):
                t1.setx(i)
                t1.sety(18 * math.sin(i / 57) + 530 - a)
        elif I == 4:
            a = random.randint(660, 665)
            t1.color(2, 2, 82)
            t1.pensize(82)
            t1.pu()
            t1.setx(-500)
            t1.sety(17 * math.sin(-500 / 56) + 530 - a)
            t1.pd()
            for i in range(-500, 500):
                t1.setx(i)
                t1.sety(17 * math.sin(i / 56) + 530 - a)
    hideturtle()
    yield


def move2():  # 雪地
    t2.pensize(1)
    t2.pu()
    t2.goto(500, -200)
    t2.right(180)
    t2.pd()
    t2.fillcolor(200, 200, 200)
    t2.begin_fill()
    for _ in range(300):
        t2.forward(4)
        t2.left(0.1)
    t2.goto(500, -506)
    t2.goto(500, -200)
    t2.end_fill()
    hideturtle()
    yield


def move3():  # 树
    a = 0
    b = -300
    c = -250 + abs(a)
    d = 40
    e = 0
    f = 0.5
    for i in range(8):
        e += 3
        t3.pu()
        t3.goto(a, b)
        t3.pd()
        t3.fillcolor(0, d, 0)
        t3.begin_fill()
        t3.goto(c * 2 + abs(a), b)
        t3.goto(-250, b + abs(3 * f * abs(c)) + e)
        t3.goto(a, b)
        t3.end_fill()
        a -= 10
        a -= e
        b += 60
        b += e
        d += 20
        f -= 0.04
    hideturtle()
    yield


def move4():  # 树桩
    t4.pu()
    t4.goto(-300, -300)
    t4.pd()
    t4.fillcolor(139, 69, 19)
    t4.begin_fill()
    t4.right(90)
    t4.fd(170)
    t4.left(90)
    t4.fd(100)
    t4.left(90)
    t4.fd(170)
    t4.end_fill()
    hideturtle()
    yield


def move5():  # 雪人
    t5.pu()  # 身体
    t5.goto(250, -400)
    t5.fillcolor(215, 215, 215)
    t5.begin_fill()
    for i in range(360):
        t5.fd(3)
        t5.left(1)
    t5.goto(250, -100)
    for i in range(360):
        t5.fd(1.8)
        t5.left(1)
    t5.end_fill()
    t5.pd()

    t5.color(205, 133, 0)  # 手
    t5.pensize(10)
    t5.pu()  # 1
    t5.goto(150, -150)
    t5.pd()
    t5.goto(50, -50)
    t5.pu()  # 11
    t5.goto(80, -80)
    t5.pd()
    t5.goto(70, -40)

    t5.pu()  # 2
    t5.goto(350, -150)
    t5.pd()
    t5.goto(450, -50)
    t5.pu()  # 22
    t5.goto(420, -80)
    t5.pd()
    t5.goto(430, -40)

    t5.color(0, 0, 0)  # 鼻子
    t5.pensize(3)
    t5.fillcolor(255, 165, 0)
    t5.begin_fill()
    t5.pu()
    t5.goto(235, -10)
    t5.pd()
    t5.goto(305, 0)
    t5.goto(235, 10)
    t5.goto(235, -10)
    t5.end_fill()

    t5.pensize(1.5)  # 眼睛
    t5.pu()
    t5.goto(223, 27)
    t5.pd()
    for i in range(300):
        t5.fd(0.3)
        t5.left(1)
    t5.fillcolor(0, 0, 0)
    t5.begin_fill()
    t5.circle(7, 360)
    t5.end_fill()
    t5.pu()
    t5.goto(272, 30)
    t5.pd()
    t5.left(30)
    t5.fillcolor(0, 0, 0)
    t5.begin_fill()
    t5.circle(7, 360)
    t5.end_fill()
    t5.left(200)
    for i in range(300):
        t5.fd(0.3)
        t5.right(1)
    t5.end_fill()

    t5.pensize(1)  # 帽子
    t5.color(255, 106, 106)
    t5.pu()
    t5.goto(190, 90)
    t5.pd()
    t5.fillcolor(255, 106, 106)
    t5.begin_fill()
    t5.goto(250, 220)
    t5.goto(310, 90)
    t5.goto(190, 90)
    t5.end_fill()
    t5.pu()
    t5.goto(265, 245)
    t5.pd()
    t5.fillcolor(238, 238, 0)
    t5.color(238, 238, 0)
    t5.begin_fill()
    t5.begin_fill()
    for i in range(9):
        t5.forward(60)
        t5.left(180 - 180 / 9)
    t5.end_fill()

    t5.pensize(3)  # 歪嘴
    t5.color(0, 0, 0)
    t5.pu()
    t5.goto(225, -40)
    t5.pd()
    t5.left(120)
    # t5.fd(100)
    for i in range(60):
        t5.fd(1)
        t5.left(1.1)
    t5.pensize(4)
    t5.pu()
    t5.right(90)
    t5.fd(10)
    t5.pd()
    t5.right(230)
    for i in range(70):
        t5.fd(0.3)
        t5.left(1.6)
    t5.pu()

    t5.pensize(1)  # 纽扣
    t5.color(0, 0, 0)
    a = -150
    t5.pu()
    t5.goto(250, a)
    t5.pd()
    t5.fillcolor(0, 0, 0)
    t5.begin_fill()
    for i in range(4):
        t5.pu()
        t5.goto(250, a)
        t5.pd()
        t5.circle(12, 360)
        a -= 40
    t5.end_fill()
    t5.pu()
    hideturtle()
    yield


def move6():  # 星空
    t6.color(255, 215, 0)  # 月亮
    t6.pu()
    t6.goto(300, 350)
    t6.pd()
    t6.fillcolor(255, 215, 0)
    t6.begin_fill()
    t6.right(60)
    for i in range(380):
        t6.fd(1.1)
        t6.left(0.7)
    t6.left(160)
    for i in range(205):
        t6.fd(1.4)
        t6.right(1.1)
    t6.end_fill()
    t6.pu()

    t6.pd()  # 星星
    j = [5, 7, 9]
    x1, x2, x3, x4 = -400, -400, -400, -400
    for i in range(8):
        if i <= 3:  # 4
            A = 1
            n = int(x1)
            m = int(x1 + 150)
            N = int(250)
            M = int(480)
            x1 += 180
        elif i <= 5:  # 2
            A = 1
            n = int(x2)
            m = int(x2 + 250)
            N = int(100)
            M = int(230)
            x2 += 300
        elif i <= 6:
            A = 1
            n = int(x3)
            m = int(x3 + 400)
            N = int(-100)
            M = int(80)
        elif i <= 7:
            A = 1
            n = int(x4)
            m = int(x4 + 400)
            N = int(-200)
            M = int(-80)
        for i in range(A):
            a = int(random.randint(n, m))
            b = int(random.randint(N, M))
            c = int(random.randint(30, 80))
            A = int(random.randint(250, 255))  # 255,215,0
            B = int(random.randint(210, 220))
            C = int(random.randint(0, 5))
            t6.pu()
            t6.goto(a, b)
            t6.pd()
            t6.color(A, B, C)
            t6.fillcolor(A, B, C)
            t6.begin_fill()
            star = random.choice(j)
            for i in range(star):
                t6.forward(c)
                t6.left(180 - 180 / star)
            t6.end_fill()
    hideturtle()
    yield


t1 = Turtle('turtle')
t1.speed(0)
t2 = Turtle('turtle')
t2.speed(6)
t3 = Turtle('turtle')
t3.speed(1)
t4 = Turtle('turtle')
t4.speed(1)
t5 = Turtle('turtle')
t5.speed(1)
t6 = Turtle('turtle')
t6.speed(1)

for i in range(3):
    taskqueue = deque()
    if i == 0:
        taskqueue.append(move1())  # Add tasks (generators)
        taskqueue.append(move2())
    elif i == 1:
        taskqueue.append(move3())  # Add tasks (generators)
        taskqueue.append(move4())
    elif i == 2:
        taskqueue.append(move5())  # Add tasks (generators)
        taskqueue.append(move6())
    while taskqueue:  # Run all of the tasks
        # Get the next task
        task = taskqueue.pop()
        try:
            # Run it to the next yield and enqueue
            next(task)
            taskqueue.appendleft(task)
        except StopIteration:
            # Task is done
            pass
hideturtle()
done()
