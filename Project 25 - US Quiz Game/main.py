from turtle import Turtle, Screen

import pandas as pd

from scoreboard import Scoreboard

import pandas

turtle = Turtle()
tim = Turtle()
screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()
screen.setup(width=800, height=600)

tim.hideturtle()
tim.penup()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

screen.update()

text = pandas.read_csv("50_states.csv")
text_states = text.state.to_list()

states_found = []
states_missed = []


print(states_found)


game_is_on = True

while game_is_on:

    user_text = screen.textinput("Enter state", "What's another state's name?").title()
    for state in text_states:
        if user_text == state:

            locate = text[text.state == user_text]
            x_cor = int(locate.x.item())
            y_cor = int(locate.y.item())

            if user_text in states_found:
                print("State is already there")
            else:
                states_found.append(user_text)
                tim.goto(x_cor, y_cor)
                tim.write(f"{user_text}")
                scoreboard.increase_score()

        elif user_text == "End":
            print(states_found)
            for i in text_states:
                if i not in states_found:
                    states_missed.append(i)

            states_data = {

                "States Missed": pd.Series(states_missed),
                "States Found": pd.Series(states_found)

            }

            df = pd.DataFrame(states_data)
            df.to_csv('Quiz Data.csv', index=False)
            break
        elif scoreboard.score == 50:
            game_is_on = False


screen.mainloop()

