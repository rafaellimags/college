import turtle

t = turtle.Turtle()

def geraPontos(i): 
   return [(i, 0), (i, i), (0, i), (0, 0)]

def desenhaPoligono(inicio, pontos, corLinha="black", corRecheio="white"):
   t.pencolor(corLinha)
   t.fillcolor(corRecheio)

   t.penup()

   t.goto(inicio)  

   t.pendown()
   t.begin_fill()

   x, y = inicio

   for ponto in pontos:  
       dx, dy = ponto
       t.goto(x + dx, y + dy)
   t.goto(inicio)  

   t.end_fill()
   t.penup()


def teste():
   cor = "green"
   # Primeiro quadrado
   quadrado = [(50, 0), (50, 50), (0, 50), (0, 0)]
   desenhaPoligono((200, 100), quadrado)

   # Segundo quadrado
   quadrado_maior = geraPontos(100)
   desenhaPoligono((-200, 230), quadrado_maior, cor)

   # Triangulo
   triangulo = [(200, 0), (100, 100), (0, 0)]
   desenhaPoligono((180, -180), triangulo, cor)


def main():
   teste()
   turtle.done()

main()