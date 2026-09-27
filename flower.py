from turtle import*
speed(0)
bgcolor("black")
pensize(2)

for i in range(20):
    for j in range(9):
        for k in range(2):
            pencolor("yellow")
            circle(40+i*5,90)
            forward(100)
            left(90)
            left(45)
done()