import math

rad = int(input('Raio: '))

def calculate_esph_area(rad):
    area = 4*math.pi*rad**2
    print(area)


calculate_esph_area(rad)