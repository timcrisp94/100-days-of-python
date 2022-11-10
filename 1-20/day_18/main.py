from turtle import Screen, Turtle

import heroes

print(heroes.gen())


tim = Turtle()
tim.shape("square")
tim.color("red")

# draw a square
def draw_square(turtle):
  turtle.forward(100)

  for i in range(3):
    turtle.left(90)
    turtle.forward(100)


# draw_square(tim)


# draw a dashed line
def draw_dashed_line(turtle):
  for i in range(10):
    turtle.forward(15)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()


# draw_dashed_line(tim)










screen = Screen()
screen.exitonclick()
