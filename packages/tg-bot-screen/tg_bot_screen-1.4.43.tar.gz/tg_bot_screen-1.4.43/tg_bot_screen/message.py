from abc import ABC, abstractmethod
from typing import Any, Self

from .callback_data import CallbackData
from .button_rows import ButtonRows

class CanBeEdited(ABC):
    @abstractmethod
    async def edit(self) -> "CanBeEdited": ...

class HasButtonRows(ABC):
    def __init__(self):
        self.button_rows: ButtonRows | None = None
        
    @abstractmethod
    def get_reply_markup(self, *args, **kwargs):
        ...
    
    def get_callback_data(self) -> list[CallbackData]:
        if self.button_rows is None:
            return []
        return self.button_rows.get_callback_data()

class SentMessage(ABC):
    def __init__(self):
        self.text: str
        self.category: str
    
    @abstractmethod
    async def delete(self): ...
    
    @abstractmethod
    def __eq__(self, other: object) -> bool: 
        ...
    
    @abstractmethod
    def clone(self) -> Self: ...
    
    @abstractmethod
    def get_unsent(self): ...

class Message(ABC):
    def __init__(self):
        self.category: str | None = None
    
    @abstractmethod
    async def send(self, user_id: int) -> SentMessage: ...
    
    @abstractmethod
    def __eq__(self, other: object) -> bool: 
        ...
    
    @abstractmethod
    def clone(self) -> Self: ...

class MediaMessage(ABC):
    def __init__(self, caption: str, button_rows: ButtonRows | None = None, 
                parse_mode: str | None = None):
        self.parse_mode = parse_mode
        self.caption = caption
        self.button_rows = button_rows
        self.category = "media"
    
    def __new__(cls, *args, **kwargs):
        assert \
            cls is not MediaMessage, \
            "Нельзя создавать экземпляры MediaMessage напрямую"
        return super().__new__(cls)


class AudioMessage(MediaMessage, Message): ...

class DocumentMessage(MediaMessage, Message): ...

class SimpleMessage(Message):
    def __init__(self, text: str, button_rows: ButtonRows | None = None, 
                    parse_mode: str | None = None):
        self.parse_mode = parse_mode
        self.text = text
        self.button_rows = button_rows
        self.category = "simple"

class PhotoMessage(MediaMessage, Message): ...

class VideoMessage(MediaMessage, Message): ...

class VideoNoteMessage(Message):
    def __init__(self, caption: str, button_rows: ButtonRows | None = None):
        self.caption = caption
        self.button_rows = button_rows
        self.category = "video_note"

class SentAudioMessage(MediaMessage, SentMessage, CanBeEdited): ...

class SentDocumentMessage(MediaMessage, SentMessage, CanBeEdited): ...

class SentSimpleMessage(SentMessage, CanBeEdited):
    def __init__(self, text: str, button_rows: ButtonRows | None = None, 
            parse_mode: str | None = None):
        self.parse_mode = parse_mode
        self.text = text
        self.button_rows = button_rows
        self.category = "simple"

class SentPhotoMessage(MediaMessage, SentMessage, CanBeEdited): ...

class SentVideoMessage(MediaMessage, SentMessage, CanBeEdited): ...

class SentVideoNoteMessage(SentMessage):
    def __init__(self, caption: str, button_rows: ButtonRows | None = None):
        self.caption = caption
        self.button_rows = button_rows
        self.category = "video_note"
