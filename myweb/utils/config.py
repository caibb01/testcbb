import json
import os
from myweb.core.runner import DATA_PATH

class JsonConfig():
    def __init__(self, path):
        self.path = path

    def get(self):
        f = open(self.path, 'r', encoding='utf-8')
        self.config = json.load(f)
        f.close()
        return self.config

    def set(self, data):
        f = open(self.path, "w", encoding='utf-8')
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()

_configPath = os.path.join(DATA_PATH, 'config.json')
conf = JsonConfig(_configPath).get()
