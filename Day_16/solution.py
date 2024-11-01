import re

from solutionPrinter import solution_println as sp

data = open("input.in","r").read().split("\n")
footprints = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def data_transformer(list_of_things):
    dict_of_sue = {}
    pattern = r'([A-Za-z\s]+\d+): ([A-Za-z]+: \d+)(?:, )?'

    for i in list_of_things:
        matches = re.findall(pattern, i)
        remaining_data = i.split(", ")[-2:]
        name = matches[0][0]
        items = {
            matches[0][1].split(": ")[0]: int(matches[0][1].split(": ")[1]),
            remaining_data[0].split(": ")[0]: int(remaining_data[0].split(": ")[1]),
            remaining_data[1].split(": ")[0]: int(remaining_data[1].split(": ")[1])
        }

        dict_of_sue[name] = items
    return dict_of_sue


def my_first_crime_scene_analysis_machine(footprints, suspects):
    output = {}
    for i in suspects:
        get_footprints = suspects[i]
        compare_score = 0
        for j in get_footprints:
            if get_footprints[j] == footprints[j]:
                compare_score+=1
        output[i] = compare_score

    return max(output, key=output.get)


def my_first_crime_scene_analysis_machine_update(footprints, suspects):
    output = {}
    for i in suspects:
        get_footprints = suspects[i]
        compare_score = 0
        for j in get_footprints:
            if j in ["cats", "trees"]:
                if get_footprints[j] > footprints[j]:
                    compare_score+=1
            elif j in ["pomeranians", "goldfish"]:
                if get_footprints[j] < footprints[j]:
                    compare_score += 1
            else:
                if get_footprints[j] == footprints[j]:
                    compare_score += 1

        output[i] = compare_score

    return max(output, key=output.get)


sp("Present is from aunt: ", my_first_crime_scene_analysis_machine(footprints, data_transformer(data)))
sp("Present is from aunt: ", my_first_crime_scene_analysis_machine_update(footprints, data_transformer(data)))