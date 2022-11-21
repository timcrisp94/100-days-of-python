from turtle import Screen, Turtle
from snake import Snake
import time


# Screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
# tracer is an animation delay, like reverb on a vocal
screen.tracer(0)
screen.title("Snake")

# create a new snake
snake = Snake()

# move snake forward
game_is_on = True
while game_is_on:    
    screen.update()
    time.sleep(0.1)

    snake.move()









screen.exitonclick()