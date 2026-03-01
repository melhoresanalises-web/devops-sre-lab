from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/")
def home():
    return jsonify(
        message="Hello from AWS CodeBuild!",
        hostname=socket.gethostname(),
        env=os.getenv("ENV", "dev")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
