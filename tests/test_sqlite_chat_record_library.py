import json

import pytest
from pew.chat.sqlite_chat_record_library import SQLiteChatRecordLibrary
from pew.chat.chat_record import ChatRecord
import datetime
from uuid import uuid4

def test_sqlite_chat_record_library():

    # Create a new instance of SQLiteChatRecordLibrary
    library = SQLiteChatRecordLibrary(":memory:")

    chatid = uuid4()
    chat_record = ChatRecord(chatid, datetime.datetime.now(), "localhost", "Sample Title", json.dumps({"message": "Hello, World!"}))
    id = library.add_record(chatid, chat_record)
    assert id == chatid

    # Test find_by_id()
    fetched_record = library.find_by_id(id)
    assert chat_record == fetched_record

    # Test get_all_records()
    all_records = library.get_all_records()
    assert len(all_records) == 1
    assert all_records[0] == chat_record