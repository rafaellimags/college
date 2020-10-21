import turtle

t = turtle.Turtle()


def check_type(triangle):
    if triangle == 1:
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(120)
        t.forward(100)
    elif triangle == 2:
        t.forward(140)
        t.left(110)
        t.forward(200)
        t.left(140)
        t.forward(200)
    else:
        t.forward(220)
        t.left(150)
        t.forward(250)
        t.left(120)
        t.forward(130)

    turtle.done()


def check_triangle(triangle):
    if triangle[0] == triangle[1] == triangle[2]:
        print('Triângulo Equilátero')
        return 1
    elif triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1] == triangle[2]:
        print('Triângulo Isósceles')
        return 2
    else:
        print('Triângulo Escaleno')
        return 3


side = 1

triangle = ()

while side < 4:
    sides = int(input(f'informe o {side}º lado do triângulo: '))
    triangle += (sides,)
    side += 1


check_type(check_triangle(triangle))
