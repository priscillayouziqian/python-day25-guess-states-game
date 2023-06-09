import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # using list comprehension:
        missing_states = [state for state in all_states if state not in guessed_states]
        # the following is not using list comprehension:
        # missing_states = []
        # #  IMPORTANT: comparing items in two lists
        # for state in all_states:  # the longer list
        #     if state not in guessed_states:  # the shorter list
        #         missing_states.append(state)

        # convert list to dataframe, then convert to excel
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # if answer_state is one of the states
    if answer_state in all_states:
        # if exists, create a turtle to write the name to the (x,y)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()






