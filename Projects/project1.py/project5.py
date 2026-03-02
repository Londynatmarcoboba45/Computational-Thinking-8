import turtle
import time
import random
from utils import *

# -----------------------------
# Section 1: Setup Window
# -----------------------------
window = turtle.Screen()
window.tracer(0)  # Makes the animation smooth

# -----------------------------
# Section 2: Create Sprites
# -----------------------------
s1 = create_sprite("Bob", 0, 0)          # Player controlled with arrow keys
s2 = create_sprite("pineapple", -200, 0) # Pineapple moves automatically
set_background("moon")

who_is_it = "pineapple"

pineapple_tags = 0
bob_tags = 0
winning_score = 10  # First to 10 tags wins

# -----------------------------
# Section 3: Player Controls (Bob)
# -----------------------------
def move_up():
    s1.goto(s1.xcor(), s1.ycor() + 8)

def move_down():
    s1.goto(s1.xcor(), s1.ycor() - 8)

def move_left():
    s1.goto(s1.xcor() - 8, s1.ycor())

def move_right():
    s1.goto(s1.xcor() + 8, s1.ycor())

window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")

# -----------------------------
# Section 4: Game Logic Function
# -----------------------------
def check_tag():
    """Check if Bob touches pineapple and update tags"""
    global pineapple_tags, bob_tags, who_is_it

    if get_distance(s1, s2) < 100:
        if who_is_it == "pineapple":
            pineapple_tags += 1
            who_is_it = "bob"
        else:
            bob_tags += 1
            who_is_it = "pineapple"

        # Reset positions after a tag
        s1.goto(200, 0)
        s2.goto(-200, 0)

# -----------------------------
# Section 5: Pineapple Automatic Movement
# -----------------------------
def move_pineapple():
    """Move pineapple in a random direction"""
    s2.setheading(random.randint(0, 360))
    s2.forward(5)

# -----------------------------
# Section 6: Game Loop
# -----------------------------
while True:
    move_pineapple()  # Make pineapple move automatically
    check_tag()       # Run tag logic
    window.update()   # Update the screen

    # Check for a winner
    if pineapple_tags >= winning_score:
        print("Pineapple Wins!")
        break
    elif bob_tags >= winning_score:
        print("Bob Wins!")
        break

    time.sleep(0.01)  # Small pause for smooth gameplay
