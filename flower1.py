from turtle import*
ht()
speed(150)
bgcolor("black")
for i in range(100):
  color("orange")
  circle(100-i)
  lt(60)
  msg= "     I AM RAHUL"
turtle.write(msg, move=True, align="left", font=("Arial", 25, "italic", "bold"))
