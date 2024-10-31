from solutionPrinter import solution_println as sp


data = "1113222113"
sample = "1"


def look_and_say(dataset):
    result = ""
    i = 0
    while i < len(dataset):
        count = 1
        while i + 1 < len(dataset) and dataset[i] == dataset[i + 1]:
            i += 1
            count += 1
        result += str(count) + dataset[i]
        i += 1
    return result


def iterator(iterations, dataset):
    for _ in range(iterations):
        dataset = look_and_say(dataset)

    return len(dataset)


sp("40 iterations:" ,iterator(40, data))
sp("50 iterations:" ,iterator(50, data))