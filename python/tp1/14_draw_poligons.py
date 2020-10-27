import turtle

t = turtle.Turtle()

screen = t.screen


def draw_sqr():
    i = 4
    while i > 0:
        t.lt(90)
        t.fd(100)
        i -= 1


def draw_crl():
    t.circle(100)


def draw_trg():
    i = 3
    while i > 0:
        t.fd(100)
        t.lt(120)
        i -= 1


screen.onkey(draw_sqr, 'q')
screen.onkey(draw_trg, 't')
screen.onkey(draw_crl, 'c')

screen.listen()

turtle.done()
