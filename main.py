# Turtle Race - Using Turtle package, learning to use to documentation, event listeners and
# having more than one instance of an object

from turtle import Turtle, Screen
import random

screen = Screen()
# Sets the size of the screen
screen.setup(width=500, height=400)

# Asks user for input via a new text window that can be stored in
# a variable like the input() function
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

# Makes 6 turtle objects with different states
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

# Checks to see if user made a bet before beginning the race
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Checks to see if turtle reached the end of the race (edge of screen)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
