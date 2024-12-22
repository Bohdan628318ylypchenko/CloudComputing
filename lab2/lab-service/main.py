from fastapi import FastAPI
import psycopg2
import os
import random
import socket


app = FastAPI()


conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("POSTGRESQL_DATABASE"),
    user=os.getenv("POSTGRESQL_USERNAME"),
    password=os.getenv("POSTGRESQL_PASSWORD")
)


@app.post("/action")
def action():
    message = " ".join(random.choices(["cat", "dog", "apple", "orange", "banana"], k=5))
    writer_ip = socket.gethostbyname(socket.gethostname())

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (writer_ip, message) VALUES (%s, %s)", (writer_ip, message))
        conn.commit()
        cursor.close()
    except Exception as e:
        return {"error": str(e)}

    return {"writer_ip": writer_ip, "message": message}


@app.get("/logs")
def get_logs():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, writer_ip, message FROM logs")
        rows = cursor.fetchall()
        cursor.close()
    except Exception as e:
        return {"error": str(e)}

    return {"logs": [{"id": row[0], "writer_ip": row[1], "message": row[2]} for row in rows]}
