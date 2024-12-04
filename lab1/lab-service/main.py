from fastapi import FastAPI
import random
import psycopg2
import socket


app = FastAPI()


conn = psycopg2.connect(
    host="db",
    port=5432,
    dbname="lab1",
    user="postgres",
    password="postgres"
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
