import turtle

t = turtle.Turtle()

rad = int(input('Raio: '))

c = 360

while c > 0:
    t.forward(rad)
    t.left(1)
    c -= 1

turtle.done()