from turtle import Turtle, Screen

screen = Screen()
# # pass in keyword arguments for readability :)
screen.setup(width=500, height=400) 
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# set y-positions list for turtle_index
y_positions = [-70, -40, -10, 20, 50, 80]

# create turtles
# it's ok to have individual objects sharing the same name
# colors differentiate them
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])



screen.exitonclick()