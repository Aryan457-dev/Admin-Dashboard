from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = "database.db"

def connect_db():
    return sqlite3.connect(DB)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

create_table()

@app.route("/")
def home():
    return "Server running"

@app.route("/departments", methods=["GET"])
def get_departments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments WHERE is_active=1")
    data = cursor.fetchall()
    conn.close()

    return jsonify([
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "created_at": row[3],
            "updated_at": row[4]
        }
        for row in data
    ])

@app.route("/departments", methods=["POST"])
def add_department():
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO departments (name, description) VALUES (?, ?)",
        (data["name"], data["description"])
    )
    conn.commit()
    conn.close()

    return {"message": "Department added"}

@app.route("/departments/<int:id>", methods=["PUT"])
def update_department(id):
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE departments SET name=?, description=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
        (data["name"], data["description"], id)
    )
    conn.commit()
    conn.close()

    return {"message": "Updated successfully"}

@app.route("/departments/<int:id>", methods=["DELETE"])
def delete_department(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE departments SET is_active=0 WHERE id=?",
        (id,)
    )
    conn.commit()
    conn.close()

    return {"message": "Deleted successfully"}

if __name__ == "__main__":
    app.run(debug=True)