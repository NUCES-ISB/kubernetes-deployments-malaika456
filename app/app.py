from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL")

def connect_db():
    try:
        conn = psycopg2.connect(DB_URL)
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database Connection Error: {conn}"
    return "Flask App is Running and Connected to PostgreSQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
