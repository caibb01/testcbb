import json


class JsonConfig():
    def __init__(self, path):
        self.path = path

    def get(self):
        f = open(self.path, 'r', encoding='ISO-8859-1')
        self.config = json.load(f)
        f.close()
        return self.config

    def set(self, data):
        f = open(self.path, "w", encoding='ISO-8859-1')
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()

