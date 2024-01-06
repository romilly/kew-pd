from abc import ABC, abstractmethod
from typing import List

from pew.prompts.prompt import Prompt


class PromptLibrary(ABC):
    @abstractmethod
    def add_prompt(self, prompt: Prompt, categories: List[str]) -> None:
        """Add a prompt to the library with a list of categories."""
        pass

    @abstractmethod
    def list_prompt_names(self) -> List[str]:
        """List all the names of the prompts in the library."""
        pass

    @abstractmethod
    def get_prompt_by_name(self, name: str) -> Prompt:
        """Retrieve a prompt by its name."""
        pass

    @abstractmethod
    def list_categories(self) -> List[str]:
        """Return a list of all categories in the library."""
        pass

    @abstractmethod
    def get_prompts_by_category(self, category: str) -> List[Prompt]:
        """Return a list of all prompts in the given category."""
        pass