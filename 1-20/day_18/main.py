from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("square")
timmy_the_turtle.color("red")

# draw a square
def draw_square(turtle):
  turtle.forward(100)

  for i in range(0, 3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)

  return turtle


# draw_square(timmy_the_turtle)

















screen = Screen()
screen.exitonclick()
