from solutionPrinter import solution_println as sp

sample = open('sample.in', 'r').read().split('"\n')
data = open('input.in', 'r').read().split('"\n')


def character_count(dataset):
    a = 0
    mx = len(dataset)
    m = 0
    for i in dataset:
        m += 1
        if m != mx:
            x = i + '"'
        else:
            x = i

        before = len(x)
        x = x.encode().decode('unicode_escape')
        after = len(x)-2
        score = before-after
        a+=score
    return a


sp("Number of decode characters from file:", character_count(data))


def character_code(dataset):
    a = 0
    mx = len(dataset)
    m = 0
    for i in dataset:
        m += 1
        if m != mx:
            x = i + '"'
        else:
            x = i
        before = len(x)
        y = '"' + x.replace('\\', '\\\\').replace('"', '\\"') + '"'
        after = len(y)
        score = after-before
        a += score
    return a


sp("Number of encode characters from file:", character_code(data))

