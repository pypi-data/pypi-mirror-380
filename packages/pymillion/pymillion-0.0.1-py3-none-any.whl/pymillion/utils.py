import json

def pretty_print(data: dict):
    print(json.dumps(data, indent=4, ensure_ascii=False))
