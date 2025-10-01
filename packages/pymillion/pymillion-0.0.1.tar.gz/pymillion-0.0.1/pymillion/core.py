import json

def create_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
