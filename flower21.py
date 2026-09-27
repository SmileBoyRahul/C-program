import turtle

def draw_petal(t, radius, angle):
    """Draws a single petal using two intersecting arcs."""
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)


# Set up canvas
screen = turtle.Screen()
screen.bgcolor("white")

# Initialize turtle
t = turtle.Turtle()
t.speed(3)

# 1. Draw the stem
t.penup()
t.goto(0, -150)
t.pendown()
t.color("green")
t.pensize(5)
t.left(90)
t.forward(200) # Draws stem up to coordinates (0, 50)

#2. Draws a leaf
t.penup()
t.goto(0, -50)
t.pendown()
t.right(45)
draw_petal(t, 60, 90) # Leaves use the same logic as petals
t.left(45)

# 3. Draws the petals (red flower)
t.penup()
t.goto(0, 50)  # Move back to the top of the stem
t.pendown()
t.pensize(2)
t.color("red")

# Loop to draw a 6-petaled flower
for _ in range(6):
    t.begin_fill()
    draw_petal(t, 100, 60)
    t.end_fill()
    t.left(360 / 6) # rotate to position the next petal

# 4. Draw the yellow center
t.penup()
t.goto(0, 35) # offset slightly to center the circle
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(15)
t.end_fill()

# keep window open 
t.hideturtle()
screen.mainloop()

