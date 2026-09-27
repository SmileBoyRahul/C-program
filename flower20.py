import turtle

#set up the screen canvas
screen = turtle.Screen()
screen.bgcolor("black") # Dark background makes colors pop

# Create and configer the turle
flower = turtle.Turtle()
flower.speed(0) # 0 is the fastest speed

# Define a list of vibrant colors
colors = ["red","purple","blue","green","orange","yellow"]

# Loop to draw overlapping circles that form the petals
for i in range(150):
    flower.color(colors[i % 6]) # Cycle through the 6 colors
    flower.circle(100 - i // 2) # Slightly decreases the size each loop
    flower.left(59)             # Rotate slightly to create a spiral effect

# Finish up 
flower.hideturtle()
screen.mainloop()