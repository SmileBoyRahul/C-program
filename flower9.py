import turtle
from turtle import*

mode("standard")
bgcolor("purple")
penup()
setx(-100)
sety(240)

pendown()
hideturtle()

begin_fill()
speed(0)

while True:
    for i in range(8):
        penup()
        forward(200)
        right(45)
        for k in range(1):
            width(4)
            for i in range(8):
                penup()
                forward(50)
                right(45)
                for j in range(8):
                    penup()
                    forward(6)
                    pendown()
                    right(45)
                    color("pink")
                    circle(10,steps=2)

end_fill()
done()                    