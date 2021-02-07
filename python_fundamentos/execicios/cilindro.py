import math

rad = float(input('Raio: '))
height = float(input('Altura: '))

def calculate_cil_areas(r, h):
    pi = math.pi
    a_base = pi*r**2
    a_side = (2*pi)*r*h
    volume = pi*r**2*h
    a_total = 2*a_base + a_side
    print(f'Area da base: {a_base:.2f}')
    print(f'Area lateral: {a_side:.2f}')
    print(f'Volume: {volume}')
    print(f'Area total: {a_total:.2f}')


calculate_cil_areas(rad, height)