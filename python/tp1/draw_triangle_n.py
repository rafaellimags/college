import turtle

t = turtle.Turtle()

side = int(input('Informe o lado do triângulo: '))

c = 3

while c > 0:
    t.forward(side)
    t.left(120)
    c -= 1

turtle.done()
    