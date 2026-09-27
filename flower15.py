from turtle import *
from colorsys import hsv_to_rgb
tracer(1000)
bgcolor("black")
setup(1000, 1000, 0, 0)

h = 0.3
for i in range(2600):
    h += 0.00025
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    goto(0, 50)

    #Base flower design 
    circle(180 - i/8, 90)
    circle(20, 119.1)
    circle(180 - i/10, -90)
    left(1)
    pensize(1 + (i % 1))
done()