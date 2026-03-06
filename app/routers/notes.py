from fastapi import APIRouter, HTTPException, status, Depends, Body, Path, Query
from typing import List, Optional, Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_session
from app.modules import Notes
from app.schemas import NotesRead, NotesCreate, NotesUpdate


router = APIRouter()

async def note_or_404(note_id: int, session: AsyncSession):
    result = await session.execute(select(Notes).where(Notes.note_id == note_id))
    note_db = result.scalar_one_or_none()

    if note_db is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return note_db


@router.post("/", response_model=NotesRead, status_code=status.HTTP_201_CREATED)
async def create_note(
    note: Annotated[
        NotesCreate,
        Body(..., description="Creating new note")],
    session: AsyncSession = Depends(get_session)
):

    new_note = Notes(title= note.title, content= note.content)
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)

    return new_note


@router.get("/", response_model=List[NotesRead])
async def get_notes(
        limit: Annotated[
            Optional[int],
            Query(title="Limit for specific amount of notes", ge=0)] = None,
        session: AsyncSession = Depends(get_session)
):

    result = await session.execute(select(Notes).order_by(Notes.note_id))
    result_list = result.scalars().all()

    if limit is not None:
        return result_list[:limit]

    return result_list

@router.get("/{note_id}", response_model=NotesRead)
async def get_notes_id(
    note_id: Annotated[
        int,
        Path(..., title="Id of note you want to see", ge=1)],
    session: AsyncSession = Depends(get_session)
):

    return await note_or_404(note_id, session)


@router.put("/{note_id}", response_model=NotesRead)
async def update_note(
        note_id: Annotated[
            int,
            Path(..., title="Id of note you want to update", ge=1)],
        note: Annotated[
            NotesUpdate,
            Body(..., description="Fully updating 1 note")],
        session: AsyncSession = Depends(get_session)
):

    note_db = await note_or_404(note_id, session)

    note_db.title = note.title
    note_db.content = note.content
    await session.commit()
    await session.refresh(note_db)

    return note_db


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(
    note_id: Annotated[
        int,
        Path(..., title="Id of note you want to delete", ge=1)],
    session: AsyncSession = Depends(get_session)
):

    note_db = await note_or_404(note_id, session)

    await session.delete(note_db)
    await session.commit()

    return