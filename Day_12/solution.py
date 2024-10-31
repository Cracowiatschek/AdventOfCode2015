import json
import re
from solutionPrinter import solution_println as sp


data = json.load(open("input.json", 'r'))


def sum_numbers_in_json(data):
    total_sum = 0

    if isinstance(data, dict):
        for value in data.values():
            total_sum += sum_numbers_in_json(value)
    elif isinstance(data, list):
        for item in data:
            total_sum += sum_numbers_in_json(item)
    elif isinstance(data, (int, float)):
        total_sum += data

    return total_sum


sp("Sum of numbers: ", sum_numbers_in_json(data))
