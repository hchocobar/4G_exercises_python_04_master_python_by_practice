# Complete the function to return the amount of days it will take to cover a route.
# HINT: You may need to import the math module for this exercise.
import math


# Implementación 1: math.ceil
def car_route(km_day, distance_to_drive):
  days = distance_to_drive / km_day
  return math.ceil(days)


# Implementación 2: utilizando la fx() del ejercicio anterior
def first_digit(number):
    digit = int(number * 10 % 10)
    return digit


def car_route_2(km_day, distance_to_drive):
  days = distance_to_drive / km_day
  # Sumamos 1 si el primer dígito decimal es mayor a 0
  return int(days) + 1 if first_digit(days) > 0 else 0


# Invoke the function with two intergers.
print(car_route(20, 40))
print(car_route(20, 45))
print(car_route(20, 71))
