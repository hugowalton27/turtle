import turtle

w = turtle.Screen()

num2 = 0
num = 0
turtle.speed(0)
turtle.hideturtle()
while True:
    turtle.circle(num)
    num += 5
    w.exitonclick
