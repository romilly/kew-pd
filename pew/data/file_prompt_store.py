import json
import os
from pew.data.prompt_store import PromptStore


class FilePromptStore(PromptStore):
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.exists(file_path):
            self.data = self.load_json()
        else:
            self.data = {}
            self.save_json()

    def load_json(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        else:
            raise FileNotFoundError('File does not exist')
        return self.data


    def save_json(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def keys(self):
        return sorted(list(self.data.keys()))

    def categories(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
            # Extract category from each prompt spec
            categories = [spec.get('category', 'default') for spec in data.values()]
            # Return sorted list of unique categories
            return sorted(set(categories))

    def get(self, key):
        return self.data.get(key, None)

    def save(self, key, data):
        self.data[key] = data
        self.save_json()

    import json

    def update(self, name: str, description: str, content: str, category: str) -> None:
        with open(self.file_path) as file:
            data = json.load(file)
            if name not in data:
                data[name] = {}
            data[name] = {}
            data[name]['description'] = description
            data[name]['content'] = content
            data[name]['category'] = category
        self.data = data
        self.save_json()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_json()