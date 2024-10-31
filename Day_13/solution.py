import itertools
from solutionPrinter import solution_println as sp
# sample = open("sample.in",'r').read().split('\n')
data = open("input.in", 'r').read().split('\n')


def get_pairs(input_data: list):
    parser = [i.split(' ')[0] for i in input_data]
    people = list(set([i for i in parser]))
    pairs = list(itertools.combinations(people, 2))

    return pairs


def data_reader(input_data: str):
    parser = input_data.split(' ')
    main = parser[0]
    guest = parser[-1][:-1]

    if "gain" in parser:
        happiness = int(parser[3])
    else:
        happiness = -int(parser[3])

    return {main: guest, "result": happiness}


def happiness_calculator(data_read, pairs):
    happiness = {}
    people = set()

    for pair in pairs:
        p1 = pair[0]
        p2 = pair[1]
        people.add(p1)
        people.add(p2)
        for i in data_read:
            keys = list(i.keys())
            if p1 == keys[0] and p2 == i[p1]:
                for j in data_read:
                    keys2 = list(j.keys())
                    if p2 == keys2[0] and p1 == j[p2]:
                        happiness[pair] = i["result"]+j["result"]

    get_variants = list(itertools.permutations(list(people)))
    result = []
    for variant in get_variants:
        get_value = 0
        key = (variant[0], variant[-1])
        key2 = (variant[-1], variant[0])

        if key in happiness:
            get_value += happiness[key]
        if key2 in happiness:
            get_value += happiness[key2]

        for i in range(len(variant)-1):
            key = (variant[i], variant[i+1])
            key2 = (variant[i+1], variant[i])

            if key in happiness:
                get_value += happiness[key]
            if key2 in happiness:
                get_value += happiness[key2]

        result.append(get_value)
    return result


metadata = [data_reader(i) for i in data]

sp("Total change in happiness: ", max(happiness_calculator(metadata, get_pairs(data))))


def me_balance(data_input:list):
    output = data_input
    parser = [i.split(' ')[0] for i in data_input]
    people = list(set([i for i in parser]))
    for i in people:
        x = f"Me would gain 0 happiness units by sitting next to {i}."
        output.append(x)
    # print(output)
    return output

metadata = [data_reader(i) for i in me_balance(data)]


sp("Total change in happiness with me: ", max(happiness_calculator(metadata, get_pairs(me_balance(data)))))
