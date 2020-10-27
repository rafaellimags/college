import turtle

t = turtle.Turtle()

sqr_amount = int(input('Informe a quantidade de quadrados: '))


def draw_form(sqr_amount):
    while sqr_amount > 0:
        draw_sqr(4)
        sqr_amount -= 1
        check_amount(sqr_amount)


def draw_sqr(n):
    while n > 0:
        t.left(90)
        t.forward(100)
        n -= 1

def check_amount(amount):
    if amount != 0:
        advance()

def advance():
    t.forward(100)


draw_form(sqr_amount)


turtle.done()
