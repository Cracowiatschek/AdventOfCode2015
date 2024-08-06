from solutionPrinter import solution_println as sp
data = list(open('input.in', 'r').read())

# position = []
position_history = [[0, 0]]

moves = {
    '>': [0, 1],
    '^': [1, 0],
    '<': [0, -1],
    'v': [-1, 0]
}


def navigator(tip, last_position, storage):
    move = moves[tip]
    new_position = [last_position[0] + move[0], last_position[1]+move[1]]
    storage.append(new_position)


for i in data:
    navigator(i, position_history[-1], position_history)

result = []
for i in position_history:
    if i not in result:
        result.append(i)


sp("At this year Santa houses count:", len(result))


robo_santa = [[0, 0]]
santa_santa = [[0, 0]]
n = 1
x = []
y = []
for i in data:
    if n % 2 != 0:
        x.append(i)
    else:
        y.append(i)
    n += 1

for i in x:
    navigator(i, robo_santa[-1], robo_santa)

for i in y:
    navigator(i, santa_santa[-1], santa_santa)

houses_positions = robo_santa + santa_santa

clean_result = []
for i in houses_positions:
    if i not in clean_result:
        clean_result.append(i)


sp("At this year Santa houses count:", len(clean_result))
