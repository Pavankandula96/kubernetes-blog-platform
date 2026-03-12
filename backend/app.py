from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "mysql")
db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "password")
db_name = os.getenv("DB_NAME", "blogdb")

def get_db_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/posts")
def posts():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM posts")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)