import turtle
import numpy as np
from numpy import pi

#setup screen
screen = turtle.Screen()
screen.colormode(255) #Enable RGB mode
screen.bgcolor('black')
screen.setup(width=800, height=800)

#Create turtle
t = turtle.Turtle()
t.speed(200)
t.penup()

## Draw pedicel

wd = 2; t.pensize(wd)
t.goto(-10, -300); t.rt(-80)
t.pendown()
for i in range(10):
    t.color((15*i, 100+15*i, 0))
    t.circle(900,(-1)**i*20)
    t.rt(90); t.fd(wd); t.lt(90)


##Draw petals

wd = 1
def draw_petal(xf, yf, d1, d2, angle=0):
    t.penup()
    t.goto(xf, yf)
    t.setheading(angle)
    t.pendown()
    for i in range(0, 180, 9):
        t.color((225, 165+int(i/2), 0))
        t.fd(d1*np.sin(i*pi/180))
        t.rt(90); t.fd(wd); t.lt(90)

    t.fd((d1+d2)*np.sin(i.pi/180))
    t.lt(90); t.fd(wd); t.rt(90)

t.fd(d2*np.sin(i*pi/180))
for i in range(o, 180, 15):
    draw_petal(105*np.cos(i*pi/90),105*np.sin(i*pi/90), 100, 70, angle=i*2-20)

## Draw central part

t.setheading(90)
t.pen(); t.goto(30, 0); t.pen()
t.color((0, 0, 0)); t.begin_fill(); t.circle(30); t.end_fill()
t.pensize(2); t.color((80, 50, 0))
for i in range(0, 360, 20):
    t.goto(15+15*np.cos(i*np.pi/180)-7.5, 15*np.sin(i*np.pi/180))
    t.circle(15)

t.penup(); t.goto(33,0); t.pendown()
t.pensize(2); t.color((120, 80, 0))
for i in range(0, 360, 7):
    t.goto(3+33*np.cos(i*np.pi/180),33*np.sin(i*np.pi/180))
    t.circle(6)

turtle.done()

