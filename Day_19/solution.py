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

configuration = config(data)

def replacements(output_text, idx_to_repl, base_text):
    return base_text[:idx_to_repl] + output_text + base_text[idx_to_repl+len(output_text)-1:]


x = []
n = 0
for i in configuration[0]:
    setting = configuration[0][i]
    input_value = setting["input_value"]
    output_value = setting["output_value"]
    molecule = configuration[1]

    mlc_cnt = molecule.count(input_value)
    mlc_idx = [match.start() for match in re.finditer(input_value, molecule)]
    for j in mlc_idx:
        if replacements(output_value, j, molecule) not in x:
            n += 1
            x.append(replacements(output_value, j, molecule))
            print(f"{input_value} => {output_value} = {molecule} => {replacements(output_value, j, molecule)}")

print(n)