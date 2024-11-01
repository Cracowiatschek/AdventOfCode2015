from itertools import combinations
from solutionPrinter import solution_println as sp


sample = [int(i) for i in open("sample.in").read().split("\n")]
data = [int(i) for i in open("input.in").read().split("\n")]


def get_combinations(containers, size):
    result = 0
    for i in range(1, len(containers)+1):
        for combo in combinations(containers, i):
            if sum(combo) == size:
                result += 1

    return result

sp("Count combination: ", get_combinations(data, 150))

def get_minimal_combinations(containers, size):
    combos = []
    for i in range(1, len(containers)+1):
        for combo in combinations(containers, i):
            if sum(combo) == size:
                combos.append(combo)
    get_minimal = min([len(i) for i in combos])
    result = sum(1 for i in combos if len(i) == get_minimal)

    return result

sp("Count combination with minimal containers: ",get_minimal_combinations(data, 150))
