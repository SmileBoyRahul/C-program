from turtle import *

speed(0)

# grass
bgcolor("green")

#sky
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()

for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

#sun
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

#cloud
penup()
goto(200, 200)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()

penup()
goto(220, 240)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(230, 215)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(180, 225)
pendown()
begin_fill()
circle(25)
end_fill()

#house
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "orange") 

#)stroke, fill)
begin_fill()

for i in range(4):
    forward(170)
    left(90)
end_fill()

#chimney
penup()
goto(20, 130)
pendown()
color("brown", "firebrick")
begin_fill()

for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

#roof
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

#window 1
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()

for i in range(4):
    forward(50)
    left(90)
end_fill()

#window 1 cross - horizontal line
penup()
goto(0, 25)
pendown()
color("black")
forward(50)

#window 1 cross - vertical line
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

#window 2
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()

for i in range(4):
    forward(50)
    left(90)
end_fill()

#window 2 cross - horizontal line
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

#window 2 cross - vertical line
penup()
goto(-55, 0)
pendown()
left(90)
forward(50)

#door
penup()
goto(-40, -97)
pendown()
right(90)
color("red")
begin_fill()

for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

#door handle
penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

hideturtle()
exitonclick()