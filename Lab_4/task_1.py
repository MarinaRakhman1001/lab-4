# TODO решите задачу

import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, "r") as f:
        json_data = json.load(f)
    All_sum = [item["score"] * item["weight"] for item in json_data]
    return round(sum(All_sum), 3)

print(task())
