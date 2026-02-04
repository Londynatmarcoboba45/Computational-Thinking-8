import turtle
import time
from utils import *

# ===== GOAL OF THE GAME =====
# Lines 5–7
# The goal of this game is to click the big Cheetos to earn Cheetos, money, and points.
# You can also press shift to spend money to buy more points, or press space to get Cheetos.

set_background("underwater")

# ===== Player variables =====
cheetos = 0   # how many Cheetos you have
money = 0     # money you earn
points = 1    # your points

# ===== Functions =====
def click_cheetos(x, y):
    """This function runs when you click the big Cheetos."""
    global cheetos, money, points
    cheetos += 1
    money += 1
    points += 1

def space_click():
    """This function runs when you press the space bar."""
    click_cheetos(0, 0)  # x, y aren’t used here, but function expects them

def buy_points():
    """This function runs when you press shift to spend money for points."""
    global money, points
    if money >= 10:  # check if player has enough money
        money -= 10
        points += 10

# ===== Keyboard controls =====
window.onkeypress(space_click, "space")  # space bar clicks the Cheetos
window.onkeypress(buy_points, "Shift_L")  # shift = buy points
window.listen()

# ===== Big Cheetos to click =====
cheetos_sprite = turtle.Turtle()
cheetos_sprite.shape("circle")  # placeholder for Cheetos image
cheetos_sprite.color("orange")
cheetos_sprite.shapesize(stretch_wid=5, stretch_len=10)  # make it big
cheetos_sprite.penup()
cheetos_sprite.goto(0, 0)  # center of screen
cheetos_sprite.onclick(click_cheetos)  # click the Cheetos to get points

# ===== Turtle to show counters =====
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-300, 200)
text.color("orange")

# ===== Game loop =====
while True:
    text.clear()  # remove old numbers
    text.write(
        f"Cheetos: {cheetos}\n"
        f"Money: {money}\n"
        f"Points: {points}\n"
        f"Next point costs 10 money",
        font=("Arial", 30, "normal")
    )

    window.update()
    time.sleep(0.01)