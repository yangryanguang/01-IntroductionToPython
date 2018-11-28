"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Guang Yang.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg
window= rg.TurtleWindow()
firstturtle=rg.SimpleTurtle('circle')
firstturtle.pen=rg.Pen('red',20)
firstturtle.speed=50
size=0
secondturtle=rg.SimpleTurtle()
secondturtle.pen=rg.Pen('blue',10)
secondturtle.speed=100


for k in range(1000):
    firstturtle.right(5)
    firstturtle.forward(size)
    secondturtle.left(5)
    secondturtle.forward(size+0.02)
    size=size+0.05

window.close_on_mouse_click()
