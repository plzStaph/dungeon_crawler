import json

def loadFromJson(obj: object, filename: str) -> None:
    """Load object attributes from json file."""
    with open(filename, 'r') as file:
        configJson = json.loads(file.read())
        for k, v in configJson.items():
            setattr(obj, k, v)

def saveToJson(obj: object, filename: str) -> None:
    """Save object attributes into json file."""
    saveDict = { k: v for k, v in obj.__dict__.items() if not callable(v) }
    with open(filename, 'w') as file:
        file.write(json.dumps(saveDict, 
            ensure_ascii=False, sort_keys=True, indent=4))