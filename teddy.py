from turtle import *
'''
#movement
forward(100)
backward(200)
goto(100, 200)

#pen control
penup()
goto(-100, 100)
pendown()
goto(-100, 0)

#angle degrees
left(90)
right(90)
setheading(270)

#circle
#circle(50)
#draws a circle that is 50 degree radius
circle(50, 180)

#color
fillcolor("pink")
pencolor("blue")
begin_fill()
circle(50)
end_fill()

#stamp
stamp()
forward(100)
stamp()
forward(100)
'''

setheading(270)
begin_fill()
circle(50, 180)
forward(80)
circle(50, 180)
forward(80)
end_fill()

#belly
fillcolor("white")
goto(10, 0)
begin_fill()
circle(40)
end_fill()

#eyes
setheading(0)
goto(30, 80)
begin_fill()
circle(20)
end_fill()
goto(70, 80)
begin_fill()
circle(20)
end_fill()

shape("circle")
fillcolor("black")
penup()
goto(30, 100)
stamp()
goto(70, 100)
stamp()

#beak
shape("triangle")
fillcolor("orange")
goto(50, 70)
setheading(270)
stamp()

#flippers
fillcolor("black")
pencolor("white")
setheading(0)
goto(0, 50)
stamp()
setheading(180)
goto(100, 50)
stamp()

#feet
shearfactor("square")
fillcolor("orange")
goto(35, -50)
stamp()
goto(65, -50)
stamp()