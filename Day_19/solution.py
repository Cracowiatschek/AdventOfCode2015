import re

from solutionPrinter import solution_println as sp

data = open("input.in").read().split("\n")
sample = open("sample.in").read().split("\n")

def config(get_input):
    output = {}
    for idx, val in enumerate(get_input[:-2]):
        output[idx] = {
            "input_value": val.split(" => ")[0],
            "output_value": val.split(" => ")[1]
        }
    input_data = get_input[-1]
    return output, input_data

configuration = config(sample)


def replacement_molecule(cfg):
    output = set()
    for i in cfg[0]:
        setting = cfg[0][i]
        input_value = setting["input_value"]
        output_value = setting["output_value"]
        molecule = cfg[1]

        positions = re.finditer(input_value, molecule)
        for match in positions:
            start, stop = match.span()
            output.add(molecule[:start] + output_value + molecule[stop:])

    return output


sp("Count of molecules: ", len(replacement_molecule(configuration)))

