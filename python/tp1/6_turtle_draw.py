import turtle

i = 0
a = 0
t = turtle.Turtle()

while i < 24:

    t.fd(150)
    t.write(str(a))
    t.bk(150)
    t.lt(15)
    a += 15

    i += 1

turtle.done()
