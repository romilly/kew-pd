from abc import ABC, abstractmethod
import json

class AbstractChatRecorder(ABC):
    @abstractmethod
    def __init__(self, db_name):
        pass

    @abstractmethod
    def add_record(self, hostname: str, data: str):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def get_all_records(self):
        pass

    @abstractmethod
    def get_record_by_id(self, id):
        pass

    @abstractmethod
    def get_records_by_hostname(self, hostname):
        pass

    @abstractmethod
    def update_record(self, id, hostname, data):
        pass

    @abstractmethod
    def delete_record(self, id):
        pass