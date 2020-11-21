import turtle

t = turtle.Turtle()
t.speed(0)
t.color('blue', 'blue')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()

turtle.done()