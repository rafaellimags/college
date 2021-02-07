import turtle

t = turtle.Turtle()

outr_sqr = 300
x_init = -150
y_init = 300
jmp = 10
btwn_circ = 80
c_spc = 15


def draw(pos, outr_sqr, jmp, btwn_circ, c_spc, n):
    print(pos)
    if n == 0:
        return

    start_pos(pos[0], pos[1])
    square1(4, outr_sqr)
    jump_inside(outr_sqr, jmp)
    square2(4, outr_sqr)
    jump_btwn(btwn_circ, 0)
    circle1(outr_sqr)
    jump_btwn((outr_sqr / 2.3) + c_spc, 270)
    circle1(outr_sqr)
    pos[0] += jmp
    pos[1] /= 2
    outr_sqr /= 2.3
    jmp = jmp / 2
    btwn_circ /= 2.4
    c_spc -= 8
    draw(pos, outr_sqr, jmp, btwn_circ, c_spc, n-1)


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


def jump_btwn(btwn_circ, head):
    t.setheading(head)
    t.penup()
    t.fd(btwn_circ)
    t.pendown()


def circle1(outr_sqr):
    t.setheading(0)
    rad = (outr_sqr / 2.3) / 2
    t.circle(-rad)


def square2(x, outr_sqr):
    if x == 0:
        return

    t.fd(outr_sqr / 2.3)
    t.rt(90)
    return square2(x-1, outr_sqr)


draw([x_init, y_init], outr_sqr, jmp, btwn_circ, c_spc, 3)
turtle.done()