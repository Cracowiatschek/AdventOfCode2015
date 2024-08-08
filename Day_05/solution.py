import re
from solutionPrinter import solution_println as sp
data = open('input.in', 'r').read().split('\n')


def contact_policy(string_list):
    n = 0
    for i in string_list:
        vowels = re.findall(r"[aeiou]", i)
        double_letters = re.findall(r"(.)\1", i)
        stop_rules = re.findall(r"ab|cd|pq|xy", i)
        if len(vowels) >= 3 and len(double_letters) >= 1 and len(stop_rules) == 0:
            n += 1
    return n


resolve = contact_policy(data)
sp("Contact policy detect nice messages:", resolve)


def contact_policy2(string_list):
    n = 0
    for i in string_list:
        double_letters = re.findall(r"(\w\w).*?\1", i)
        aba_rule = re.findall(r"(.).\1", i)
        if len(double_letters) == 1 and len(aba_rule) >= 1:
            n += 1
    return n


resolve2 = contact_policy2(data)
sp("New contact policy detect nice messages:", resolve2)
