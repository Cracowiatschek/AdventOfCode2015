from solutionPrinter import solution_println as sp

sample = open("sample.in","r").read().split("\n")
data = open("input.in","r").read().split("\n")



def read_recipe(recipe):

    decode_recipe = {}
    for i in recipe:
        ingredient = i.split(": ")[0]
        properties = i.split(": ")[1].split(", ")
        properties_decoded = {}
        for p in properties:
            name = p.split(" ")[0]
            unit = int(p.split(" ")[1])
            properties_decoded[name] = unit
        decode_recipe[ingredient] = properties_decoded

    return decode_recipe


def get_proportions(target, length, start=0, current=[]):
    if length == 1:
        # Ostatnia liczba musi być równa target, aby suma była zgodna z celem
        if target >= start:
            yield current+[target]
        return

    for i in range(start, target+1):
        yield from get_proportions(target-i, length-1, 0, current+[i])


def find_the_best_proportions(recipe, spoons = 100, calories_mode = False):
    ingredients_count = len(recipe)
    ingredients = [i for i in recipe if i != "calories"] if calories_mode is True else [i for i in recipe if i]
    properities = []

    test_borad = list(get_proportions(spoons, ingredients_count))

    for idx, itm in enumerate(test_borad):
        scoreboard = {
            "capacity": 0,
            "durability": 0,
            "flavor": 0,
            "texture": 0
        } if calories_mode is False else {
            "capacity": 0,
            "durability": 0,
            "flavor": 0,
            "texture": 0,
            "calories": 0
        }
        for index, item in enumerate(itm):
            scoreboard["capacity"] += recipe[ingredients[index]]["capacity"]*item
            scoreboard["durability"] += recipe[ingredients[index]]["durability"]*item
            scoreboard["flavor"] += recipe[ingredients[index]]["flavor"]*item
            scoreboard["texture"] += recipe[ingredients[index]]["texture"]*item
            if calories_mode is True:
                scoreboard["calories"] += recipe[ingredients[index]]["calories"] * item

        score = 1
        if calories_mode is True:
            if scoreboard["calories"] == 500:
                for s in scoreboard:
                    if s != "calories":
                        if scoreboard[s] < 0:
                            scoreboard[s] = 0
                for j in scoreboard:
                    if j != "calories":
                        score *= scoreboard[j]
                properities.append(score)
        else:
            for s in scoreboard:
                if scoreboard[s] < 0:
                    scoreboard[s] = 0
            for j in scoreboard:
                score *= scoreboard[j]
            properities.append(score)

    return max(properities)

sp("Total score is: ", find_the_best_proportions(read_recipe(data), calories_mode = False))
sp("Total score for 500 calories is: ", find_the_best_proportions(read_recipe(data), calories_mode = True))
