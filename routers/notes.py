from models import Notes
from schemas import Note,NoteUpdate,NoteResponse
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends,APIRouter,HTTPException
from auth import get_current_user
from datetime import datetime
router = APIRouter(prefix="/notes",tags=["/NOTES"])
@router.post("/",status_code=201)
def create_notes(note:Note,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    note_data = Notes(
        title = note.title,
        content = note.content,
        created_at = datetime.utcnow(),
        owner_id = current_user.id

    )
    db.add(note_data)
    db.commit()
    db.refresh(note_data)
    return note_data
@router.get("/",response_model=list[NoteResponse])
def get_notes(title:str | None = None,limit:int=10,skip:int=0,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    notes = db.query(Notes).filter(Notes.owner_id == current_user.id)
    if title:
        notes = db.query(Notes).filter(Notes.title == title)
    return notes.offset(skip).limit(limit).all()
@router.get("/{note_id}",response_model=NoteResponse)
def get_note(note_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    note = db.query(Notes).filter(Notes.id == note_id,Notes.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404,detail="note not found")
    return note
@router.put("/{note_id}",response_model=NoteResponse)
def update_note(note_id:int,update:NoteUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    note = db.query(Notes).filter(Notes.id == note_id,Notes.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404,detail="note not found")
    if update.title is not None:
        note.title = update.title
    db.commit()
    db.refresh(note)
    return note
@router.delete("/{note_id}")
def delete_note(note_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    note = db.query(Notes).filter(Notes.id == note_id,Notes.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404,detail="note not found")
    db.delete(note)
    db.commit()
    return {"success":"note deleted"}
