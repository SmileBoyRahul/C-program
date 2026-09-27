from turtle import *

def flower():
    for i in range(300):
        bgcolor('black')
        color('cyan')
        speed(500)
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(190)

flower()
hideturtle()
mainloop()