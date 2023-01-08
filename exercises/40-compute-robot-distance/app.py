# La distancia entre dos coordenadas (0, 0)(b, h) es igual a la hipotenusa del triángulo con base (0, b) y altura (0, h)
import math


def compute_distance(instructions):
    # entrada: UP 5 DOWN 3 LEFT 3 RIGHT 2
    # índices: 0  1 2    3 4    5 6     7
    steps = instructions.split(" ")
    origin = [0, 0]
    x = origin[0] + int(steps[1]) - int(steps[3])
    y = origin[1] + int(steps[5]) - int(steps[7])
    position = [x, y]
    distance = (int(round(math.sqrt(position[0] ** 2 + position[1] ** 2))))
    return distance


movimientos = 'UP 5 DOWN 3 LEFT 3 RIGHT 2'
print(compute_distance(movimientos))
