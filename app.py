from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello 12-factor! This is an example of 1. Codebase 2. Dependencies 7. Port binding 11. Logs"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    print("Server started on port", 8000)
    app.run(host="0.0.0.0", port=port)
