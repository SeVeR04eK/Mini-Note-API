# Notes API 1 (FastAPI Learning Project)

## Description

This is a small educational CRUD API built with FastAPI as part of backend learning practice.

The project implements basic operations for managing notes:

- Create a note  
- Get all notes (+the specified amount of notes)
- Get a single note by ID  
- Update a note  
- Delete a note  


---

## Technologies Used

- Python  
- FastAPI  
- Pydantic  
- Uvicorn 
- SQLAlchemy

---

## Project Structure

```
notes-api/
├── app/
│   ├── routers/
│   │   └── notes.py
│   ├── database.py
│   ├── main.py
│   ├── modules.py
│   └── schemas.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## How to Run

1. Create virtual environment:

        python -m venv venv

2. Activate it:

    Windows:

       venv\Scripts\activate

    Mac/Linux:

       source venv/bin/activate


3. Install dependencies:

        pip install -r requirements.txt

4. Create database mini_note_api:
   
    pysql:

         CREATE DATABASE mini_notes_api

5. Run init file:

   pysql:

          \c my_database
          \i your_full/path/init.sql

6. Create .env file

   Windows:

          echo DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/mini_notes_api > .env

   Linux:

          echo "DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/mini_notes_api" > .env

7. Run the server:

       uvicorn main:app --reload

8. Open in browser:

http://127.0.0.1:8000/docs
Swagger UI documentation will be available there.

---

## Available Endpoints

| Method | Endpoint        | Description         |
|--------|-----------------|---------------------|
| POST   | /notes          | Create a new note   |
| GET    | /notes          | Get all notes       |
| GET    | /notes/{note_id} | Get note by ID     |
| PUT    | /notes/{note_id} | Update note        |
| DELETE | /notes/{note_id} | Delete note        |

---

## Notes
 
- This project is part of backend development practice.
- Have fun!