import turtle

w = turtle.Screen()
t = turtle
fd = turtle.forward
rt = turtle.right
lt = turtle.left

num = 0

t.color("red")
w.bgcolor("white")
t.speed(0)
t.hideturtle()

while num <= 1440:
    t.forward(1)
    t.right(1)
    num += 1
    if num == 360:
        t.penup()
        lt(90)
        fd(50)
        t.pendown()
    if num == 720:
        t.penup()
        lt(90)
        fd(50)
        t.pendown()
    if num == 1080:
        t.penup()
        lt(90)
        fd(50)
        t.pendown()


w.exitonclick()