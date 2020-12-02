import math

rad = int(input('Raio: '))

def calculate_circ_area(rad):
    area = math.pi*rad**2
    print(f'Área: {area}')


calculate_circ_area(rad)