import itertools
from solutionPrinter import solution_println as sp

sample = open('sample.in', 'r').read().split("\n")
data = open('input.in', 'r').read().split("\n")


def read_data(dataset):
    orient_express = {}

    for i in dataset:
        places = i.split('to')
        p1 = places[0].replace(" ","")
        p2 = places[1].split("=")[0].replace(" ","")
        route = int(places[1].split("=")[1])
        if p1 not in orient_express:
            orient_express[p1] = []
        if p2 not in orient_express:
            orient_express[p2] = []
        orient_express[p1].append([p2, route])
        orient_express[p2].append([p1, route])

    return orient_express


def get_distance(city1, city2):
    for destination, distance in x[city1]:
        if destination == city2:
            return distance
    return None


def calculator_route(navigation, mode):
    if mode == "min":
        target = []
        for i in navigation:
            x = []
            travel = [i]
            limit = len(navigation)-1
            last = i
            while len(x) < limit:
                research = navigation[last]

                p, r = [i[0] for i in research if i[0] not in travel], [i[1] for i in research if i[0] not in travel]
                get_value = min(r)

                ix = r.index(get_value)
                x.append(get_value)
                travel.append(p[ix])
                last = p[ix]
            target.append(sum(x))
        return min(target)
    elif mode == "max":
        cities = list(navigation.keys())

        all_routes = itertools.permutations(cities)

        max_distance = 0

        for route in all_routes:
            distance = sum(get_distance(route[i], route[i + 1]) for i in range(len(route) - 1))
            if distance > max_distance:
                max_distance = distance
        return max_distance
    else:
        print("Wrong mode! Avaible: [\"min\",\"max\"]")


x = read_data(data)

sp("Minimal distance:", calculator_route(x,"min"))
sp("Maximal distance:", calculator_route(x,"max"))


