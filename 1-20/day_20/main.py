from turtle import Screen, Turtle

# Screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")

# Build snake by individual segments, starting with a snake at position 0 and moving left
# for each position, add a white block segment to the snake (segments[])
starting_positions = [(0, 0), (-20, 0) (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

# move snake forward










screen.exitonclick()