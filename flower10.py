import turtle
import colorsys
p=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
p.speed(0)
p.pensize(1.8)
h=1
n=80
for i in range(400):
    c=colorsys.hsv_to_rgb(h,0.9,1)
    p.color(c)
    p.circle(-i+1,95)
    h+=1/n
    p.rt(85)
    p.lt(35)
turtle.done()    