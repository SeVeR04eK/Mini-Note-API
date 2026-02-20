from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class Note(BaseModel):
    note_id: int
    title: str
    content: str

class NoteCreate(BaseModel):
    title: str
    content: str

notes = [
    Note(note_id= 1, title= "note.title", content= "note.content"),
    Note(note_id= 2, title= "note.title2", content= "note.content2")
]


@app.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteCreate) -> Note:
    note_id = len(notes) + 1
    new_note = Note(note_id= note_id, title= note.title, content= note.content)
    notes.append(new_note)
    return new_note


@app.get("/notes")
async def get_notes(limit: Optional[int] = None) -> List[Note]:
    if limit is not None:
        if limit < 0:
            raise HTTPException(status_code=400, detail="Invalid query parameter")
        return [note for note in notes[:limit]]

    return [note for note in notes]

@app.get("/notes/{note_id}")
async def get_notes_id(note_id: int) -> Note:
    if 0 < note_id <= len(notes):
        return notes[note_id-1]
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/notes/{note_id}")
async def update_note(note_id: int, note: NoteCreate) -> Note:
    if 0 < note_id <= len(notes):
        new_note = Note(note_id= note_id, title= note.title, content= note.content)
        notes[note_id - 1] = new_note
        return new_note
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    if 0 < note_id <= len(notes):
        notes.pop(note_id - 1)
        return
    """Note: ID logic simplified for in-memory storage"""

    raise HTTPException(status_code=404, detail="Item not found")