# 📝 Personal Notes API

A secure RESTful Notes API built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**.  
Users can register, log in, and manage their own personal notes with full CRUD functionality, filtering, and pagination.

---

## 🚀 Features

- 🔐 JWT Authentication
- 🔑 Password Hashing with Passlib + Bcrypt
- 👤 User Registration & Login
- 📝 Create, Read, Update & Delete Notes
- 🔒 User-specific data access
- 🔍 Filter notes by title
- 📄 Pagination using `skip` and `limit`
- 🗄️ PostgreSQL Database
- 🔄 Alembic Database Migrations
- ⚙️ Environment Variables with `.env`
- 📚 Automatic API Documentation with Swagger UI

---

## 🛠️ Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy ORM**
- **Alembic**
- **Pydantic**
- **JWT (python-jose)**
- **Passlib + Bcrypt**
- **Python Dotenv**

---

## 📂 Project Structure

```text
personal-note-api/
│
├── routers/
│   ├── auth_routes.py
│   └── notes.py
│
├── auth.py
├── config.py
├── database.py
├── models.py
├── schemas.py
├── main.py
│
├── alembic/
├── alembic.ini
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔑 Authentication Endpoints

### Register

```
POST /auth/register
```

Example:

```json
{
    "email": "user@gmail.com",
    "password": "password123"
}
```

---

### Login

```
POST /auth/login
```

Returns:

```json
{
    "access_token": "...",
    "token_type": "bearer"
}
```

Use the token in the **Authorize** button inside Swagger.

---

## 📝 Notes Endpoints

Create Note

```
POST /notes/
```

Get All Notes

```
GET /notes/
```

Get Single Note

```
GET /notes/{note_id}
```

Update Note

```
PUT /notes/{note_id}
```

Delete Note

```
DELETE /notes/{note_id}
```

---

## 🔍 Filtering

Search notes by title:

```
GET /notes/?title=python
```

---

## 📄 Pagination

Get first 10 notes:

```
GET /notes/?skip=0&limit=10
```

Get next 10 notes:

```
GET /notes/?skip=10&limit=10
```

Pagination uses SQLAlchemy's:

```python
.offset(skip).limit(limit)
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/personal-note-api.git
```

Go into the project:

```bash
cd personal-note-api
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
alembic upgrade head
```

Start server:

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 👨‍💻 Author

Built as a backend practice project using **FastAPI** to strengthen authentication, CRUD operations, filtering, pagination, and REST API design principles.