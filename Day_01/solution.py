from solutionPrinter import solution_println as sp
data = open('input.in', 'r').read()

upstairs = data.count("(")
downstairs = data.count(")")

result = upstairs-downstairs

sp("Santa go to the floor number:", result)

floor = 0
step = 0
for i in list(data):
    step += 1
    if floor != -1:
        if i == "(":
            floor += 1
        else:
            floor -= 1
    else:
        break

sp("Santa's position when he first enter to basement was:", step-1)
