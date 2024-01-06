from abc import ABC, abstractmethod
from uuid import UUID
from typing import List

from pew.chat.chat_record import ChatRecord


class ChatRecordLibrary(ABC):

    @abstractmethod
    def add_record(self, id: UUID, record: ChatRecord) -> UUID:
        """Add a record to the store and return its ID."""
        pass

    @abstractmethod
    def find_by_id(self, id: UUID) -> ChatRecord:
        """Find a record by its ID."""
        pass

    @abstractmethod
    def get_all_records(self) -> List[ChatRecord]:
        """Return all records in the store."""
        pass