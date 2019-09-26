import math
def roots_by_for():
    a = [2, 4, 9, 16, 25]
    res = []
    for x in a:
        res.append(math.sqrt(x))
    return res

def roots_by_map():
    return list(map(math.sqrt, [2, 4, 9, 16, 25]))

def roots_by_generator():
    return [math.sqrt(x) for x in [2, 4, 9, 16, 25]]
