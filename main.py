import turtle
import pandas

# #to get coordinats of the words
# def get_coord(x,y):
#     print(x, y)
# turtle.onscreenclick(get_coord)

screen = turtle.Screen()
image = "body-part-anatomy1.gif"
screen.addshape(image)
turtle.shape(image)
#screen.mainloop()
#
data = pandas.read_csv("eng-dutch.csv")
body_parts = data.English.to_list()
named = []


while len(named) < 13:
    answer = screen.textinput(title="Body parts", prompt="Name body parts in English").lower()
    if answer == "exit":
        break
    if answer in body_parts:
        named.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        new_data = data[data.English == answer]
        t.goto((int(new_data.x)), int(new_data.y))
        t.write(new_data.Dutch.item(), font=("Arial", 28, "bold"))





