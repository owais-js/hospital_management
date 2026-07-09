# 🏥 Hospital Management System API

A RESTful **Hospital Management System API** built with **FastAPI**, **SQLAlchemy**, **MySQL**, and **Alembic**. The project follows a clean, modular architecture and implements complete CRUD (Create, Read, Update, Delete) operations for managing **Patients**, **Doctors**, and **Staff**.

This project was developed to demonstrate backend development concepts including database design, REST APIs, ORM integration, request validation, and database migrations.

---

## 🚀 Features

* 👨‍⚕️ Patient Management (CRUD)
* 🩺 Doctor Management (CRUD)
* 👥 Staff Management (CRUD)
* Request & Response Validation using Pydantic
* MySQL Database Integration
* SQLAlchemy ORM
* Database Versioning with Alembic
* Environment Variable Configuration
* Modular Project Structure
* Interactive API Documentation with Swagger UI
* RESTful API Design

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **MySQL**
* **Alembic**
* **Pydantic**
* **Uvicorn**
* **Python Dotenv**

---

## 📁 Project Structure

```text
hospital_management/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── staff.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── crud/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── staff.py
│   │
│   ├── models/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── staff.py
│   │
│   ├── schemas/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── staff.py
│   │
│   └── __init__.py
│
├── .env
├── .gitignore
├── alembic.ini
├── main.py
├── README.md
└── requirements.txt
```

---

## 🗄️ Database Models

### 👨‍⚕️ Patient

* ID
* Name
* Age
* Gender
* Phone

### 🩺 Doctor

* ID
* Name
* Gender
* Specialization
* Qualification
* Phone
* Experience

### 👥 Staff

* ID
* Name
* Gender
* Designation
* Department
* Phone
* Salary

---

## 📌 API Endpoints

### Patient Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/patients`      | Create Patient    |
| GET    | `/patients`      | Get All Patients  |
| GET    | `/patients/{id}` | Get Patient by ID |
| PUT    | `/patients/{id}` | Update Patient    |
| DELETE | `/patients/{id}` | Delete Patient    |

---

### Doctor Endpoints

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| POST   | `/doctors`      | Create Doctor    |
| GET    | `/doctors`      | Get All Doctors  |
| GET    | `/doctors/{id}` | Get Doctor by ID |
| PUT    | `/doctors/{id}` | Update Doctor    |
| DELETE | `/doctors/{id}` | Delete Doctor    |

---

### Staff Endpoints

| Method | Endpoint      | Description            |
| ------ | ------------- | ---------------------- |
| POST   | `/staff`      | Create Staff Member    |
| GET    | `/staff`      | Get All Staff Members  |
| GET    | `/staff/{id}` | Get Staff Member by ID |
| PUT    | `/staff/{id}` | Update Staff Member    |
| DELETE | `/staff/{id}` | Delete Staff Member    |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/hospital_management.git
cd hospital_management
```

### Create Virtual Environment

```bash
python -m venv hospital_env
```

### Activate Virtual Environment

**Windows**

```bash
hospital_env\Scripts\activate
```

**Linux / macOS**

```bash
source hospital_env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=hospital_db
```

---

## 🔄 Database Migration

Generate Migration

```bash
alembic revision --autogenerate -m "Initial Migration"
```

Apply Migration

```bash
alembic upgrade head
```

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

Application URL

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🏗️ Project Architecture

The project follows a layered architecture to improve readability, maintainability, and scalability.

* **Models** → Database tables using SQLAlchemy
* **Schemas** → Request and response validation using Pydantic
* **CRUD** → Database operations and business logic
* **API** → REST endpoints and routing
* **Core** → Database connection and configuration
* **Alembic** → Database migration management

---

## 🎯 Learning Objectives

This project demonstrates:

* Building REST APIs with FastAPI
* CRUD Operations
* SQLAlchemy ORM
* MySQL Integration
* Database Migrations with Alembic
* Dependency Injection
* Environment Variable Management
* Clean Project Architecture
* Request Validation using Pydantic
* API Documentation using Swagger

---

## 📜 License

This project is created for learning and educational purposes.
