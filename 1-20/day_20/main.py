from turtle import Screen, Turtle

# Screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")

# Snake
starting_positions = [(0, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)












screen.exitonclick()