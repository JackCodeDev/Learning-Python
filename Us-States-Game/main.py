import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

new_data_state = data["state"].tolist()

score = 0
guess_states = []

while len(guess_states) < 50:
    answer_states = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_states in new_data_state:
        guess_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        score += 1
        data_state_new = data[data["state"] == answer_states]
        # data_x = data_state_new["x"]
        # x = data_x.tolist()
        # data_y = data_state_new["y"]
        # y = data_y.tolist()
        # x.extend(y)
        # new_x_y = tuple(x)
        t.goto(float(data_state_new.x), float(data_state_new.y))
        t.write(answer_states)
    elif answer_states == "Exit":
        missing_state = []
        for state in new_data_state:
            if state not in guess_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

