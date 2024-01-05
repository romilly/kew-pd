import sqlite3
import uuid
import json
from datetime import datetime

from pew.chat.recorder import AbstractChatRecorder


class SQLiteChatRecorder(AbstractChatRecorder):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                hostname TEXT NOT NULL,
                data TEXT NOT NULL
            )
        """)

    def add_record(self, hostname: str, data: str):
        id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        self.cursor.execute("""
            INSERT INTO chats (id, timestamp, hostname, data) VALUES (?, ?, ?, ?)
        """, (id, timestamp, hostname, json.dumps(data)))
        self.conn.commit()

    def __del__(self):
        try:
            self.close()
        except:
            pass
            # what else can I do?

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def get_all_records(self):
        self.cursor.execute("SELECT * FROM chats")
        return self.cursor.fetchall()

    def get_record_by_id(self, id):
        self.cursor.execute("SELECT * FROM chats WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def get_records_by_hostname(self, hostname):
        self.cursor.execute("SELECT * FROM chats WHERE hostname = ?", (hostname,))
        return self.cursor.fetchall()

    def update_record(self, id, hostname, data):
        self.cursor.execute("""
            UPDATE chats SET hostname = ?, data = ? WHERE id = ?
        """, (hostname, json.dumps(data), id))
        self.conn.commit()

    def delete_record(self, id):
        self.cursor.execute("DELETE FROM chats WHERE id = ?", (id,))
        self.conn.commit()