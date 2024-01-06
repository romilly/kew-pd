import sqlite3
from typing import List

from pew.prompts.prompt import Prompt
from pew.prompts.prompt_library import PromptLibrary


class SQLitePromptLibrary(PromptLibrary):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prompts (
                name TEXT PRIMARY KEY,
                contents TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categories (
                name TEXT PRIMARY KEY
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS PromptCategories (
                prompt_name TEXT,
                category_name TEXT,
                FOREIGN KEY(prompt_name) REFERENCES Prompts(name),
                FOREIGN KEY(category_name) REFERENCES Categories(name),
                PRIMARY KEY (prompt_name, category_name)
            )
        """)

    def add_prompt(self, prompt: Prompt, categories: List[str]) -> None:
        with self.conn:
            self.cursor.execute("INSERT INTO Prompts (name, contents, description) VALUES (?, ?, ?)",
                                (prompt.name, prompt.contents, prompt.description))
            for category in categories:
                self.cursor.execute("INSERT OR IGNORE INTO Categories (name) VALUES (?)", (category,))
                self.cursor.execute("INSERT INTO PromptCategories (prompt_name, category_name) VALUES (?, ?)",
                                    (prompt.name, category))

    def list_prompt_names(self) -> List[str]:
        self.cursor.execute("SELECT name FROM Prompts")
        return [name[0] for name in self.cursor.fetchall()]

    def get_prompt_by_name(self, name: str) -> Prompt:
        self.cursor.execute("SELECT * FROM Prompts WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result:
            return Prompt(result[0], result[1], result[2])
        return None

    def list_categories(self) -> List[str]:
        self.cursor.execute("SELECT name FROM Categories")
        return [category[0] for category in self.cursor.fetchall()]

    def get_prompts_by_category(self, category: str) -> List[Prompt]:
        self.cursor.execute("""
            SELECT Prompts.* FROM Prompts JOIN PromptCategories 
            ON Prompts.name = PromptCategories.prompt_name
            WHERE PromptCategories.category_name = ?
        """, (category,))
        results = self.cursor.fetchall()
        return [Prompt(result[0], result[1], result[2]) for result in results]

    def get_prompt_categories(self, prompt_name: str) -> List[str]:
        self.cursor.execute("""
            SELECT category_name FROM PromptCategories
            WHERE prompt_name = ?
        """, (prompt_name,))
        return [category[0] for category in self.cursor.fetchall()]