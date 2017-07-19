from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)

### Write your code below:
begin_fill('green')
color('green')
for b in range(3):
    t.forward(120)
    t.right(120)
end_fill('green')
### code from before: pendown()right(60)forward(100)right(60)forward(100)left(60)forward(100)penup()
# Close window on click.
exitonclick()
