import turtle
 
t = turtle.Turtle()
t.speed(0)
side = 200
for i in range(70):
   t.forward(side)
   t.right(120)
   side = side - 3


turtle.done()