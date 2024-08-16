from solutionPrinter import solution_println as sp
data = open("input.in", 'r').read().split("\n")
sample = open("sample.in", 'r').read().split("\n")


def int_or_str(x):
    try:
        y = int(x)
        return y
    except ValueError:
        return x.replace(' ', '')


def processor(input_x, input_y, operator):
    if operator == "&":
        x_resolution = (input_x & input_y) & 0xFFFF
        return x_resolution
    elif operator == "|":
        x_resolution = (input_x | input_y) & 0xFFFF
        return x_resolution
    elif operator == "<<":
        x_resolution = (input_x << input_y) & 0xFFFF
        return x_resolution
    elif operator == ">>":
        x_resolution = (input_x >> input_y) & 0xFFFF
        return x_resolution
    elif operator == "~":
        x_resolution = (~input_x) & 0xFFFF
        return x_resolution
    else:
        x_resolution = input_x
        return x_resolution


def parser(dataset):
    mapping = {}

    for i in dataset:
        source, target = i.split("->")[0], i.split("->")[1].replace(' ', '')
        if "AND" in source:
            x = int_or_str(source.split(" ")[0])
            y = int_or_str(source.split(" ")[2])
            mapping[target] = [x, "&", y]
        elif "OR" in source:
            x = int_or_str(source.split(" ")[0])
            y = int_or_str(source.split(" ")[2])
            mapping[target] = [x, "|", y]
        elif "LSHIFT" in source:
            x = int_or_str(source.split(" ")[0])
            y = int_or_str(source.split(" ")[2])
            mapping[target] = [x, "<<", y]
        elif "RSHIFT" in source:
            x = int_or_str(source.split(" ")[0])
            y = int_or_str(source.split(" ")[2])
            mapping[target] = [x, ">>", y]
        elif "NOT" in source:
            x = int_or_str(source.split(" ")[1])
            mapping[target] = [x, "~"]
        else:
            x = int_or_str(source.split(" ")[0])
            mapping[target] = x

    return mapping


operations_map = parser(data)


def read_and_process(operations):
    result = {}

    while 'a' not in result:

        for y in operations:
            if y not in result:
                get_value = operations[y]
                if type(get_value) is int: # starter
                    result[y] = get_value
                if type(get_value) is str and get_value in result:  # simple send node a to node b
                    search_value = result[get_value]
                    if type(search_value) is int:
                        result[y] = search_value
                if type(get_value) is list:
                    m = get_value[0]
                    oper = get_value[1]

                    if len(get_value) == 2 and m in result:  # NOT
                        search_m = result[m]
                        x = processor(search_m, 0, oper)
                        result[y] = x
                    elif len(get_value) == 2 and m not in result:
                        continue
                    elif len(get_value) == 3:
                        n = get_value[2]
                        if m in result or n in result:  # if something is in result
                            if m in result and n in result:  # if a and b in result
                                search_m = result[m]
                                search_n = result[n]
                                x = processor(search_m, search_n, oper)
                                result[y] = x
                            elif type(m) is int:  # if only b in result
                                search_n = result[n]
                                x = processor(m, search_n, oper)
                                result[y] = x
                            elif type(n) is int:  # if only an in result
                                search_m = result[m]
                                x = processor(search_m, n, oper)
                                result[y] = x
                            else:
                                continue
                        else:
                            continue
    return result


solution_part_one = read_and_process(operations_map)
sp("Signal provided to wire 'a' is: ", solution_part_one['a'])
