# TODO решите задачу
import json

FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    res = [round(dict_['score'] * dict_['weight'], 3) for dict_ in json_data]
    return sum(res)

print(task())
