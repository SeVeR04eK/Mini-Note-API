from pydantic import BaseModel, Field
from typing import Annotated

class NotesBase(BaseModel):
    title: Annotated[str, Field(..., title="Note title",  max_length=50)]
    content: Annotated[str, Field(..., title="Note content")]

class NotesCreate(NotesBase):
    pass

class NotesUpdate(NotesBase):
    pass

class NotesRead(NotesBase):
    note_id: Annotated[int, Field(..., title="Note id")]

    class Config:
        from_attributes = True