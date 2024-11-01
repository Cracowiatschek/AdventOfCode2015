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


sp("The best reindeer lead at: ", max(result))


def raindeer_raid(raindeer, test_time):
    leaderboard = {i: {"points": 0, "travel": 0, "stamina": raindeer[i]["stamina"],
                       "speed": raindeer[i]["speed"], "rest":  raindeer[i]["rest"]} for i in raindeer}

    for i in range(test_time):
        actual_time = i+1
        for j in leaderboard:
            raid_cycle = leaderboard[j]["stamina"]+leaderboard[j]["rest"]
            last_cycle = actual_time % raid_cycle

            if last_cycle <= leaderboard[j]["stamina"] and actual_time <= raid_cycle:
                leaderboard[j]["travel"] += leaderboard[j]["speed"]
            elif last_cycle < leaderboard[j]["stamina"] and actual_time > raid_cycle:
                leaderboard[j]["travel"] += leaderboard[j]["speed"]
            else:
                leaderboard[j]["travel"] += 0
        get_leader_travel = max(leaderboard[i]["travel"] for i in leaderboard)
        get_leader = [i for i in leaderboard if leaderboard[i]["travel"] == get_leader_travel]

        for j in get_leader:
            leaderboard[j]["points"] += 1

    get_winner = max([leaderboard[i]["points"] for i in leaderboard])
    return get_winner+1


sp("The best reindeer has: ", raindeer_raid(read_data(data), travel_time))
