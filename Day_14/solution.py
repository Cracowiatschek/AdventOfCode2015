from solutionPrinter import solution_println as sp


sample = open("sample.in", 'r').read().split("\n")
data = open("input.in", 'r').read().split("\n")


def read_data(inp_data):
    output = {}
    for i in inp_data:
        parser = i.split(' ')
        output[parser[0]] = {"speed": int(parser[3]), "stamina": int(parser[6]), "rest":int(parser[-2])}
    return output


def travel_calculator(raindeer, test_time):
    cycle = raindeer["stamina"]+raindeer["rest"]
    travel_at_cycle = raindeer["stamina"] * raindeer["speed"]

    result = int(test_time/cycle) * travel_at_cycle
    last_cycle = cycle - test_time%cycle
    if last_cycle <= raindeer["stamina"]:
        result += raindeer["stamina"]*raindeer["speed"]
    else:
        result += travel_at_cycle
    return result


travel_time = 2503
result = map(lambda i, j=travel_time: travel_calculator(read_data(data)[i],j), read_data(data))

sp("The best raindeer lead at: ", max(result))

def raindeer_raid(raindeer, test_time):
    for i in range(test_time):
        for j in raindeer:
