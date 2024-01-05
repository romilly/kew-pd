from abc import ABC, abstractmethod

class PromptStore(ABC):
    @abstractmethod
    def keys(self):
        pass

    @abstractmethod
    def categories(self):
        """Return a sorted list of categories."""
        pass

    @abstractmethod
    def get(self, key):
        pass


    @abstractmethod
    def update(self, name, description, content, category):
        """Creates or Updates a prompt with the provided description, content and category."""
        pass

    @abstractmethod
    def delete(self, key):
        pass