from pydantic import BaseModel

class NotesBase(BaseModel):
    title: str
    content: str

class NotesCreate(NotesBase):
    pass

class NotesUpdate(NotesBase):
    pass

class NotesRead(NotesBase):
    note_id: int

    class Config:
        from_attributes = True