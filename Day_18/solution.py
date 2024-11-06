from solutionPrinter import solution_println as sp


config = {
    "stay_on": [2,3],
    "switch_on": [3],
    "on": "#",
    "off": "."
}

neighbours = {
    "up_left":{
        "row": -1,
        "column": -1
    },
    "up_central":{
        "row": -1,
        "column": 0
    },
    "up_right":{
        "row": -1,
        "column": 1
    },
    "central_left": {
        "row": 0,
        "column": -1
    },
    "central_right": {
        "row": 0,
        "column": 1
    },
    "down_left": {
        "row": 1,
        "column": -1
    },
    "down_central": {
        "row": 1,
        "column": 0
    },
    "down_right": {
        "row": 1,
        "column": 1
    }
}

sample = open("sample.in", "r").read().split("\n")
data = open("input.in", "r").read().split("\n")


def giphy(input_data, steps, neighbours_data, config_data, corners = False):

    get_table = [list(i) for i in input_data]
    rows_limit_idx = len(get_table)-1
    columns_limit_idx = len(get_table[0])-1
    corners_position = [[0, 0], [0, rows_limit_idx], [rows_limit_idx, 0], [rows_limit_idx, columns_limit_idx]]

    if corners is True:
        cache_table = []
        for rit, row in enumerate(get_table):
            cache_row = []
            for cit, column in enumerate(row):
                if [rit, cit] in corners_position:
                    cache_row.append(config_data["on"])
                else:
                    cache_row.append(column)
            cache_table.append(cache_row)
        get_table=cache_table


    for i in range(steps):
        cache_table = []
        for rit, row in enumerate(get_table):
            cache_row = []
            for cit, column in enumerate(row):
                count_on_states = 0
                for n in neighbours_data:
                    try:
                        row_idx = rit - neighbours_data[n]["row"]
                        column_idx = cit - neighbours_data[n]["column"]

                        if [row_idx, column_idx] in corners_position and corners is True:
                            # print(row_idx, column_idx)
                            get_value = config_data["on"]
                        else:
                            get_value = get_table[row_idx][column_idx]

                        if get_value == config_data["on"] and row_idx >= 0 and column_idx >= 0:
                            count_on_states+=1

                    except Exception as e:
                        g = e
                if ((column == config_data["on"] and count_on_states in config_data["stay_on"])
                        or (column == config_data["off"] and count_on_states in config_data["switch_on"])):
                    cache_row.append(config_data["on"])
                elif [rit, cit] in corners_position and corners is True:
                    cache_row.append(config_data["on"])
                else:
                    cache_row.append(config_data["off"])
            cache_table.append(cache_row)
        get_table = cache_table

    lights_on_count = 0

    for i in get_table:
        for j in i:
            if j == config["on"]:
                lights_on_count += 1
    return lights_on_count


sp("Number of lights is on: ", giphy(data, 100, neighbours, config))

sp("Number of lights is on: ", giphy(data, 100, neighbours, config, True))
