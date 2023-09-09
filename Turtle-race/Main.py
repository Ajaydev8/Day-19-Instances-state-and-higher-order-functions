from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color").lower()
rainbow_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
]
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.goto(x=-230, y=y[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            if turtle.color()[0] == user_bet:
                print(f"congratulation your turtle {user_bet} won ")
                is_race_on = False
            else:
                print(f"Your turtle {user_bet} lost.")
                is_race_on = False



screen.exitonclick()
