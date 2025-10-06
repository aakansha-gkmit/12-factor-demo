# 🧩 12-Factor App – Minimal Python Flask Example

This repository is a **minimal, single-file example** demonstrating core ideas from the [Twelve-Factor App](https://12factor.net/) methodology using **Python** and **Flask**. It's intentionally small so you can run it locally, inspect how configuration and dependencies work, and use it as a simple demo.

---

## What this project demonstrates (short)

- **Codebase** — single Git repository.
- **Dependencies** — listed in `requirements.txt`.
- **Config** — uses environment variables (`PORT`) instead of hard-coding.
- **Port binding** — Flask binds directly to a port.
- **Logs** — output goes to stdout (terminal).
- **Admin process** — easy to add one-off scripts if needed.

---

## Project structure

```
12-factor-demo/

├── app.py             # Minimal Flask app
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## `app.py` (example)

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello 12-factor! This is an example of 1. Codebase 2. Dependencies 7. Port binding 11. Logs"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Server starting on port {port}...")
    app.run(host='0.0.0.0', port=port)
```

> If you already have `app.py`, you can replace its contents with the snippet above or verify it follows the same pattern.

---

## `requirements.txt`

```
Flask
```

---

## Setup & Run

1. **Clone (or create) the project folder**

```bash
git clone https://github.com/<your-username>/12-factor-demo.git
cd 12-factor-demo
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
# or on some systems
pip3 install -r requirements.txt
```

3. **Run locally**

```bash
python app.py
# or
python3 app.py
```

You should see output similar to:

```
Server starting on port 8000...
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://10.x.x.x:8000
```

Open your browser at `http://127.0.0.1:8000` to see the app response.

---

## Change configuration (no code edits)

Change ports or other configuration using environment variables. Example (macOS / Linux):

```bash
export PORT=9000
python app.py
```

Windows (PowerShell):

```powershell
$env:PORT = "9000"
python app.py
```

This demonstrates the *Config* factor — changing runtime behavior without changing source.

---

## How these lines map to 12 factors (brief)

- **Codebase** — this entire app is tracked in one repo.
- **Dependencies** — managed by `requirements.txt` and `pip`.
- **Config** — `PORT` is read from the environment.
- **Port binding** — Flask exposes an HTTP service via `app.run(host='0.0.0.0', port=...)`.
- **Logs** — `print()` outputs to stdout (terminal).

---

