def check_triangle(triangle):
    if triangle[0] == triangle[1] == triangle[2]:
        print('Triângulo Equilátero')
    elif triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1] == triangle[2]:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')


side = 1

triangle = ()

while side < 4:
    sides = int(input(f'informe o {side}º lado do triângulo: '))
    triangle += (sides,)
    side += 1


check_triangle(triangle)
