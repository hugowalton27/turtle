import turtle

w = turtle.Screen()

fd = turtle.forward
lt = turtle.left
rt = turtle.right

def circle(speed):
    turtle.speed(speed)
    turtle.hideturtle()
    x = 0
    while x < 360:
        rt(1)
        fd(1)
        x += 1

circle("fastest")
w.exitonclick