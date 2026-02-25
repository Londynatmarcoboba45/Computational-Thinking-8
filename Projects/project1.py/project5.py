import turtle, math, time, random
from utils import *

# Section 1: Setup
s1 = create_sprite("Bob",0,0)
s2 = create_sprite("pineapple")
set_background("moon")
who_is_it="pineappple"

# Section 2: Controls (Arrow keys to move the minion and banana)

            










def move_up_1 (w):
    x = s1.xcor()
    y = s1.ycor()  

def move_down_1 (s):
    x = s1.xcor()
    y = s1.ycor() - 3
    s1.goto(x,y)
    
def move_left_1 (a):
    x = s1.xcor() - 3
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right_1 (d): 
    x = s1.xcor() + 8
    y = s1.ycor() 
    s1.goto(x,y)






def move_up_1(i):
    x = s1.xcor()
    y = s1.ycor(-200) + 8
    s1.goto(x,y)
        
def move_down_1(k):
    x = s1.xcor()
    y = s1.ycor() - 5
    s1.goto(x,y)
    
def move_left_1(l):
    x = s1.xcor() - 9
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right_1(j): 
    x = s1.xcor() + 8
    y = s1.ycor() 
    s1.goto(x,y)








window.listen()
window.onkeypress(move_up_1, "Up")
window.onkeypress(move_down_1, "Down")
window.onkeypress(move_left_1, "Left")
window.onkeypress(move_right_1, "Right")

for i in range(10000000000):

    if get_distance(s1, s2) < 100:
        if who_is_it == "pineapple":
            pineapple_tags += 1
        elif who_is_it == "bob":
            s1.goto(200,0)
            s2.goto(-200,0)
            bob_tags += 1
            who_is_it = "pineapple"

    if i >= 30 * 100:
        break

    time.sleep(0.01)
    window.update()
