from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to DevOps Mastery Challenge - DEVELOP!"


@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/about")
def about():
    return "DevOps Mastery Challenge - Flask Application"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
