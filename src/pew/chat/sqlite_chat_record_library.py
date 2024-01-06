import datetime
import json
import sqlite3
from uuid import UUID

from pew.chat.chat_record import ChatRecord
from pew.chat.chat_record_library import ChatRecordLibrary


class SQLiteChatRecordLibrary(ChatRecordLibrary):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ChatRecords (
                id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                hostname TEXT NOT NULL,
                title TEXT NOT NULL,
                conversation TEXT NOT NULL
            )
        """)

    def add_record(self, id: UUID, record: ChatRecord):
        with self.conn:
            self.cursor.execute("""
                INSERT INTO ChatRecords (id, timestamp, hostname, title, conversation)
                VALUES (?, ?, ?, ?, ?)
            """, (str(id), record.timestamp.isoformat(), record.hostname, record.title, json.dumps(record.conversation)))
        return id

    def find_by_id(self, id: UUID) -> ChatRecord:
        self.cursor.execute("""
            SELECT * FROM ChatRecords WHERE id = ?
        """, (str(id),))
        result = self.cursor.fetchone()
        if result is not None:
            return ChatRecord(UUID(result[0]), datetime.datetime.fromisoformat(result[1]), result[2], result[3], json.loads(result[4]))
        return None

    def get_all_records(self):
        self.cursor.execute("""
            SELECT * FROM ChatRecords
        """)
        result = self.cursor.fetchall()
        return [ChatRecord(UUID(record[0]), datetime.datetime.fromisoformat(record[1]), record[2], record[3], json.loads(record[4])) for record in result]