from turtle import Screen, Turtle
import time

# Screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
# tracer is an animation delay, like reverb on a vocal
screen.tracer(0)
screen.title("Snake")

# Build snake by individual segments, starting with a snake at position 0 and moving left
# for each position, add a white block segment to the snake (segments[])
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# move snake forward
game_is_on = True
while game_is_on:
    # delay to smooth animation see: tracer   
    time.sleep(.1)

    # * loop through range of segments in reverse
    # * range(start, stop, step) *
    for seg_num in range(len(segments) - 1, 0, -1):
        # second to last segment x-coor
        new_x = segments[seg_num - 1].xcor()
        # second to last segment y-coor        
        new_y = segments[seg_num - 1].ycor()        
        # last segment go to second to last segment
        segments[seg_num].goto(new_x, new_y)
    screen.update()









screen.exitonclick()