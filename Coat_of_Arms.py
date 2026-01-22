# Section 1 - Your code
from utils import *
set_background("summer")

s1 = create_sprite("basketball", 100, 100)
s2 = create_sprite("flil", -100, 100)
s3 = create_sprite("cardinal", -100, -100)
s4 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("Black")
message1.write("Londyn",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Mamba Mentality",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()