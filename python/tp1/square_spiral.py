import turtle
 
t = turtle.Turtle()
t.speed(0)
side = 200
for i in range(100):
   t.forward(side)
   t.right(90) 
   side = side - 2

turtle.done()