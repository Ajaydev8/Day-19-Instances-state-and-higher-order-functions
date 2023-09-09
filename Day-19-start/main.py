from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed("fastest")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    tim.right(10)


def move_anticlockwise():
    tim.left(10)


def clear_turtle_screen():
    tim.clear()
    tim.penup()
    tim.setheading(0)
    tim.goto(0, 0)
    tim.pendown()


# In order to make the screen listen
screen.listen()
# We have to bind a function that will be triggered when a particular key is hit on the keyboard.
screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=move_anticlockwise, key="a")
screen.onkey(fun=clear_turtle_screen, key="c")

# Prevent the screen from disappearing
screen.exitonclick()
