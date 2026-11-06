
import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to DevOps Mastery Challenge - Successfully Merged!"


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


@app.route("/about")
def about():
    return "DevOps Mastery Challenge - Flask Application"


@app.route("/db-health")
def db_health():
    db_host = os.getenv("DB_HOST", "redis-db")
    db_port = int(os.getenv("DB_PORT", "6379"))

    try:
        with socket.create_connection((db_host, db_port), timeout=3) as connection:
            connection.sendall(b"*1\r\n$4\r\nPING\r\n")
            response = connection.recv(1024).decode().strip()

        if response == "+PONG":
            return jsonify({
                "database": "UP",
                "host": db_host,
                "response": "PONG"
            })

        return jsonify({"database": "DOWN", "response": response}), 503

    except OSError as error:
        return jsonify({
            "database": "DOWN",
            "error": str(error)
        }), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
