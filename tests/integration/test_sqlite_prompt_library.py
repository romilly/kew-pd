import pytest
from pew.prompts.sqlite_prompt_library import SQLitePromptLibrary
from pew.prompts.prompt import Prompt

def test_add_prompt():
    library = SQLitePromptLibrary(':memory:')
    prompt1 = Prompt('prompt1', 'contents1', 'description1')
    categories1 = ['cat1', 'cat2']

    library.add_prompt(prompt1, categories1)

    assert 'prompt1' in library.list_prompt_names()
    assert 'cat1' in library.list_categories()
    assert 'cat2' in library.list_categories()

def test_get_prompt_by_name():
    library = SQLitePromptLibrary(':memory:')
    prompt_1 = Prompt('prompt_1', 'contents1', 'description1')
    categories1 = ['cat1', 'cat2']
    library.add_prompt(prompt_1, categories1)

    prompt_2 = Prompt('prompt_2', 'contents2', 'description2')
    categories2 = ['cat1', 'cat3']
    library.add_prompt(prompt_2, categories2)

    stored_prompt = library.get_prompt_by_name('prompt_1')
    assert stored_prompt == prompt_1

def test_get_prompts_by_category():
    library = SQLitePromptLibrary(':memory:')
    prompt_1 = Prompt('prompt_1', 'contents1', 'description1')
    categories1 = ['cat1', 'cat2']
    library.add_prompt(prompt_1, categories1)

    prompt_2 = Prompt('prompt_2', 'contents2', 'description2')
    categories2 = ['cat1', 'cat3']
    library.add_prompt(prompt_2, categories2)

    prompts_in_cat1 = library.get_prompts_by_category("cat1")

    assert len(prompts_in_cat1) == 2  # both prompts belong to 'cat

    stored_prompt = library.get_prompt_by_name('prompt_1')
    assert stored_prompt == prompt_1
