import numpy as np
import matplotlib.pyplot as plt
from solutionPrinter import solution_println as sp
data = open('input.in', 'r').read().split("\n")


def get_data(dataset):
    data_out = []
    for i in dataset:
        settings = []
        if "on" in i:
            settings.append("on")
        elif "off" in i:
            settings.append("off")
        else:
            settings.append("toggle")

        text = i.split(' ')
        settings.append([int(text[-3].split(',')[0]), int(text[-3].split(',')[1])])
        settings.append([int(text[-1].split(',')[0]), int(text[-1].split(',')[1])])

        data_out.append(settings)

    return data_out


tips = get_data(data)
test_tips = [
    ["on", [0, 0], [999, 999]],
    ["toggle", [100, 0], [200, 0]],
    ["off", [499, 499], [500, 500]]
]


def rendering(hints, name):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for i in hints:
        x1, y1 = i[1][0], i[1][1]
        x2, y2 = i[2][0]+1, i[2][1]+1
        for j in range(x1, x2):
            for k in range(y1, y2):
                if i[0] == "on":
                    matrix[j][k] = 1
                elif i[0] == "off":
                    matrix[j][k] = 0
                else:
                    if matrix[j][k] == 1:
                        matrix[j][k] = 0
                    else:
                        matrix[j][k] = 1
    plt.imshow(np.array(matrix), cmap="grey", interpolation="nearest")
    plt.savefig(name)
    return matrix


resolution = sum([sum(i) for i in rendering(tips, "PartOne.png")])
sp("Sum turn on lights:", resolution)


def rendering_different_lights(hints, name):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for i in hints:
        x1, y1 = i[1][0], i[1][1]
        x2, y2 = i[2][0]+1, i[2][1]+1
        for j in range(x1, x2):
            for k in range(y1, y2):
                if i[0] == "on":
                    matrix[j][k] += 1
                elif i[0] == "off":
                    x = matrix[j][k]
                    x -= 1
                    matrix[j][k] = max(0, x)
                else:
                    matrix[j][k] += 2
    plt.imshow(np.array(matrix), cmap="grey", interpolation="nearest")
    plt.savefig(name)
    return matrix


resolution2 = sum([sum(i) for i in rendering_different_lights(tips, "PartTwo.png")])
sp("Sum of lightness:", resolution2)
