import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor(-200) + 8
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 5
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 9
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 8
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()
def draw () :
    s1.pendown ()

window.onkeypress (move_left, "a")
window.onkeypress (move_right, "d")
window.onkeypress (draw, "c")

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()