from solutionPrinter import solution_println as sp
import hashlib
data = open('input.in', 'r').read()


def md5_search(key: str, start_search: str):
    seed = 0
    x = ""
    limit = len(start_search)
    while x[0:limit] != start_search:
        seed += 1
        resolution = key.encode("UTF-8") + str(seed).encode("UTF-8")
        h = hashlib.md5(resolution)
        x = h.hexdigest()
        if x[0:limit] == start_search:
            return seed


resolve_p1 = md5_search(data, "00000")
sp("Answer for part one: ", resolve_p1)

resolve_p2 = md5_search(data, "000000")
sp("Answer for part two: ", resolve_p2)
