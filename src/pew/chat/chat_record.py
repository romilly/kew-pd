from dataclasses import dataclass
import datetime
import json
from uuid import UUID

@dataclass(frozen=True)
class ChatRecord:
    id: UUID
    timestamp: datetime.datetime
    hostname: str
    title: str
    conversation: json