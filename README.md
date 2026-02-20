# Notes API 1 (FastAPI Learning Project)

## Description

This is a small educational CRUD API built with FastAPI as part of backend learning practice.

The project implements basic operations for managing notes:

- Create a note  
- Get all notes  
- Get a single note by ID  
- Update a note  
- Delete a note  

The application uses in-memory storage (a Python list), meaning data is not persisted after server restart.  
This is intentional, as the project focuses on learning FastAPI fundamentals before integrating a database.

---

## 🚀 Technologies Used

- Python  
- FastAPI  
- Pydantic  
- Uvicorn  

---

## 📂 Project Structure

```
notes-api/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

1. Create virtual environment:

        python -m venv venv

2. Activate it:

    Windows:

       venv\Scripts\activate

    Mac/Linux:

       source venv/bin/activate


3. Install dependencies:

        pip install -r requirements.txt

4. Run the server:

       uvicorn main:app --reload

5. Open in browser:

http://127.0.0.1:8000/docs
Swagger UI documentation will be available there.

---

## 📬 Available Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST   | /notes | Create a new note |
| GET    | /notes | Get all notes |
| GET    | /notes/{note_id} | Get note by ID |
| PUT    | /notes/{note_id} | Update note |
| DELETE | /notes/{note_id} | Delete note |

---

## ⚠️ Notes

- Data is stored in memory.  
- IDs are simplified for learning purposes.  
- This project is part of backend development practice.