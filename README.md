# AQMTECH Assessment – Image Gallery Application

A full-stack image gallery application built using **React (Vite)** for the frontend and **FastAPI + MySQL** for the backend.  
The application provides a Google Images–style grid layout with a responsive right-side image preview.

---

## 🚀 Tech Stack

### Frontend
- React (Vite)
- JavaScript
- Ant Design 
- CSS 

### Backend
- FastAPI
- SQLAlchemy ORM
- MySQL
- Pydantic
- Uvicorn

---

## 📁 Project Structure
AQMTECH-ASSESSMENT/
├── backend/
│ ├── db/
│ │ └── db.py
│ ├── model/
│ │ └── model.py
│ ├── schema/
│ │ └── schema.py
│ ├── images/
│ ├── main.py
│ ├── .env
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── api/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── assets/
│ │ └── styles/
│ ├── vite.config.js
│ └── package.json
│
└── README.md


---

## ⚙️ Prerequisites

Ensure you have the following installed:

- Node.js ≥ 18
- Python ≥ 3.10
- MySQL ≥ 8
- Git

---

## 🖥️ Backend Setup (FastAPI)

### 1️⃣ Clone the repository

git clone https://github.com/your-username/aqmtech-assessment.git
cd aqmtech-assessment

### 2️⃣ Create & activate virtual environment
cd backend
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Configure environment variables (backend)
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/aqmtech_db

### 5️⃣ Start backend server
uvicorn backend.main:app --reload

### 6️⃣ Verify database connection
GET /db_check

### 7️⃣ Install frontend dependencies
cd frontend
npm install
