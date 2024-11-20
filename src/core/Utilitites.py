import json

class Utilities:

    @classmethod
    def load_json(filename: str) -> dict:
        with open(filename, "r") as f:
            data: dict = json.load(f)
        return data