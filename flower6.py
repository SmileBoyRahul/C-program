from turtle import*
import colorsys
title("NIIN KM")
bgcolor("black")
tracer(2)
c=3

for i in range(200):
    p = colorsys.hsv_to_rgb(c, 1, 0.99)
    c+=0.003
    pencolor(p)
    goto(0,0)
    forward(50+i)
    right(160)
    forward(90+i)
    left(140)
    forward(80)
    left(190)
    forward(180)
    right(120)
    forward(10)
    right(100)
    forward(120)
    forward(30)
    left(190)
    forward(50)
    right(200)
    forward(40)
    hideturtle()

done()    

