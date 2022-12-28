import turtle
import colorsys

t = turtle.Turtle()
s=turtle.Screen()
t.hideturtle()
t.pensize(1)
s.bgcolor('black')
t.speed(0)
hue=0.0

for i in range(400):
    color=colorsys.hsv_to_rgb(hue,1,1)
    t.pencolor(color)
    hue+=0.005
    t.forward(i*1.5)
    t.right(150)
turtle.done()
