# FastAPI Task Management API

Production-ready RESTful API built using FastAPI and PostgreSQL.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic
- Uvicorn
- Render (Deployment)

## Features
- CRUD operations for task management
- PostgreSQL database integration
- ORM-based database models
- Request validation using Pydantic schemas
- Structured modular architecture
- Deployed backend service

## Project Structure

```bash
fastapi-todo/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── .gitignore
```

## API Documentation
Swagger Docs:
https://fastapi-todo-server-i8u6.onrender.com/docs

## Live Deployment
https://fastapi-todo-server-i8u6.onrender.com

## Installation (Local Setup)

1. Clone repository
2. Create virtual environment
3. Install dependencies

pip install -r requirements.txt

4. Run server

uvicorn main:app --reload

## Environment Variables

DATABASE_URL=your_postgresql_connection_string

## Learning Focus
This project demonstrates:
- REST API development
- Database schema design
- ORM integration
- Backend deployment
- Clean architecture structure
