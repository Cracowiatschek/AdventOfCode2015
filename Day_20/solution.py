from solutionPrinter import solution_println as sp
from math import isqrt

data = 36000000


def calculate_gifts_optimized(house_number):
    gifts = 0
    for i in range(1, isqrt(house_number) + 1):
        if house_number % i == 0:
            gifts += i * 10
            if i != house_number // i:
                gifts += (house_number // i) * 10
    return gifts


def calculate_gifts_with_limit(house_number):
    gifts = 0
    for i in range(1, isqrt(house_number) + 1):
        if house_number % i == 0:
            if house_number // i <= 50:
                gifts += i * 11
            if i != house_number // i and i <= 50:
                gifts += (house_number // i) * 11
    return gifts


def search_house_number(target_gifts, limit_mode = False):
    house_number = 1
    while True:
        if limit_mode is False:
            gifts = calculate_gifts_optimized(house_number)
        else:
            gifts = calculate_gifts_with_limit(house_number)

        if gifts >= target_gifts:
            break
        house_number += 1
    return house_number

sp("House number: ", search_house_number(data))
sp("House number: ", search_house_number(data, limit_mode = True))

