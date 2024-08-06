from solutionPrinter import solution_println as sp
data = [[int(j) for j in i.split('x')] for i in open('input.in', 'r').read().split('\n')]


def surface_calculator(x, y, z):
    x_y = 2 * x * y
    x_z = 2 * x * z
    y_z = 2 * y * z
    reserve = min(x_y, x_z, y_z)/2

    return sum([x_y, x_z, y_z, reserve])


result = sum([surface_calculator(i[0], i[1], i[2]) for i in data])
sp("Square feet of wrapping paper :", result)


def ribbon_calculator(x, y, z):
    mx = max([x, y, z])
    wrap = 2*(sum([x, y, z])-mx) + (x * y * z)
    return wrap


ribbon = sum([ribbon_calculator(i[0], i[1], i[2]) for i in data])
sp("Feet of ribbon :", ribbon)
