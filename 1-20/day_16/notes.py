"""
moving on from procedural programming to object oriented programming
* the car metaphor

object oriented programming
ex: you are running a restaurant:
      you are the receptionist,
      you are the server,
      you are the cook, etc

    oop:
      people trained for individual jobs:
        you are the manager of these people, but they are autonomous

a waiter object has attributes and methods

we are trying to model real life objects. those objects have things and they can do.
an object is how we add data and functions to a thing

a waiter class or blueprint produces individual waiter objects
"""
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)


print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()