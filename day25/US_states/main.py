from queue import Empty
import turtle
import pandas as pd

screen  = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
game_is_on = True
guessed_states = []
counter = 0

while game_is_on:
    answer_state = screen.textinput(title=f"{counter}/50 States Correct", prompt="Guess a state?").title()

    selected_state = data[data.state == answer_state]
    
    if selected_state.empty == False:
        guessed_states.append(answer_state)
        state_name = selected_state.state.to_list()[0]
        xcord = int(selected_state["x"])
        ycord = int(selected_state["y"])

        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto((xcord, ycord))
        new_turtle.write(state_name)
        counter += 1
    
    if counter == 50 or answer_state == "Exit":
        states_not_guessed = []
        for state in data.state:
            if state not in guessed_states:
                states_not_guessed.append(state)
        
        if len(states_not_guessed) > 0:
            new_data = pd.DataFrame(states_not_guessed)
            new_data.to_csv("States not Guessed correctly.csv")
        game_is_on = False
  

