from turtle import Screen, Turtle

# Screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")

# Snake
segment_one = Turtle("square")
segment_one.color("white")

segment_two = Turtle("square")
segment_two.color("white")
segment_two.setposition(-10.00, 0.00)

segment_three = Turtle("square")
segment_three.color("white")
segment_three.setposition(10.00, 0.00)











screen.exitonclick()