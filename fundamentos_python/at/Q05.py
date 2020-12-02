import turtle

t = turtle.Turtle()

outr_sqr = 300
x_init = -150
y_init = 300
jmp = 10


def draw(pos, outr_sqr, jmp, n):
    if n == 0:
        return

    start_pos(pos[0], pos[1])
    square1(4, outr_sqr)
    jump_inside(outr_sqr, jmp)
    print(jmp)
    square2(4)
    jump_btwn(80, 0)
    circle1()
    jump_btwn((outr_sqr / 2.3) + 15, 270)
    circle1()
    pos[0] += 12
    pos[1] /= 2
    outr_sqr /= 2.3
    jmp = jmp / 2
    draw(pos, outr_sqr, jmp, n-1)


def start_pos(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    return x + 10, y / 2


def square1(x, outr_sqr):
    if x == 0:
        return

    t.fd(outr_sqr)
    t.rt(90)
    return square1(x-1, outr_sqr)


def jump_inside(outr_sqr, jmp):
    t.fd(outr_sqr / 2.1)
    t.rt(90)
    t.penup()
    t.fd(jmp)
    t.pendown()


def jump_btwn(l, head):
    t.setheading(head)
    t.penup()
    t.fd(l)
    t.pendown()


def circle1():
    t.setheading(0)
    rad = (outr_sqr / 2.3) / 2
    t.circle(-rad)


def square2(x):
    if x == 0:
        return

    t.fd(outr_sqr / 2.3)
    t.rt(90)
    return square2(x-1)


draw([x_init, y_init], outr_sqr, jmp, 2)
turtle.done()