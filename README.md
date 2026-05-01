# 🚀 Admin Dashboard – Department Management System

## 📌 Overview

This project is a **full-stack web application** that allows an administrator to manage departments.
It supports **Create, Read, Update, and Delete (CRUD)** operations with a simple and clean UI.

---

## 🌐 Live Demo

* 🔗 Frontend (Netlify):
  https://prismatic-beignet-c6bc97.netlify.app

* 🔗 Backend API (Render):
  https://admin-dashboard-wv1b.onrender.com/departments

---

## 📂 GitHub Repository

https://github.com/Aryan457-dev/Admin-Dashboard

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python (Flask)
* Flask-CORS

### Database

* SQLite

### Deployment

* Frontend: Netlify
* Backend: Render

---

## ⚙️ Features

* ✅ Add new departments
* ✅ View all departments
* ✅ Update department details
* ✅ Delete department (Soft delete)
* ✅ Persistent data storage
* ✅ Fully deployed application

---

## 📁 Project Structure

Admin-Dashboard/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md

---

## 🚀 Installation & Setup (Local)

### 1. Clone Repository

git clone https://github.com/Aryan457-dev/Admin-Dashboard.git

cd Admin-Dashboard

---

### 2. Setup Backend

cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py

---

### 3. Run Frontend

Open `frontend/index.html` in your browser

---

## 🔗 API Endpoints

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | /departments      | Get all departments    |
| POST   | /departments      | Add department         |
| PUT    | /departments/{id} | Update department      |
| DELETE | /departments/{id} | Soft delete department |

---

## 🧪 Usage

1. Open the frontend application
2. Add a department using the form
3. Edit or delete existing departments
4. Data will be stored in the database

---

## ⚠️ Notes

* Soft delete is implemented using `is_active` flag
* Backend runs on Flask API
* CORS is enabled for frontend-backend communication

---

## 📌 Author

**Aryan Dabholkar**

---

## ⭐ Acknowledgement

This project was developed as part of an internship assignment to demonstrate full-stack development skills including deployment.

---
