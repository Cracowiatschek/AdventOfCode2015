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
        return input_x & input_y
    elif operator == "|":
        return input_x | input_y
    elif operator == "<<":
        return input_x << input_y
    elif operator == ">>":
        return input_x >> input_y
    elif operator == "~":
        return ~input_x
    else:
        return input_x


mapping = {}
test = []
for i in data:
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

research = {}
cache = []
locks = []

for i in mapping:
    try:
        len(mapping[i])
        continue
    except TypeError:
        research[i] = mapping[i]

print(mapping)
while len(research) != len(mapping):

    for i in research:
        input_x = research[i]
        if i not in research or i not in locks:
            for j in mapping:
                input_y = ''
                operator = ''

                try:
                    if len(mapping[j]) == 2:  # get NOT
                        input_y = int_or_str(mapping[j][0])
                        operator = mapping[j][1]
                    else:
                        operator = mapping[j][1]
                        input_y = int_or_str(mapping[j][2])
                except TypeError:
                    continue

                if type(input_y) is int:
                    x = processor(input_x, input_y, operator)
                    locks.append(j)
                    cache.append([j, x])
                elif input_y in research:
                    input_y = research[input_y]
                    x = processor(input_x, input_y, operator)
                    locks.append(j)
                    cache.append([j, x])
                else:
                    continue
    for i in cache:
        research[i[0]] = i[1]
    print(research)

print(len(research))
print(research['a'])

    #         if type(is_int(j))==int:
    #             research[i] = mapping[i]
    # if len(research) >= 2:
    #     print(research)
    #     start = "0"

    # if is_int_bool(x):
    #     research[j] = research[i] + x
    #     continue
    # elif x in research:
    #     research[j] = research[i] + research[x]
    #     continue
    # else:
    #     cache[j] = mapping[j]
    #     continue
