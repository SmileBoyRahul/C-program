from turtle import *
speed(20)
bgcolor("black")
clr=('cyan','yellow','magenta','red')
radius=200
penup()
goto(x=200, y=100)
pendown()

for i in range(150):
    color(clr[i%4])
    circle(radius,-180)
    rt(90)
    radius=radius-1

done()