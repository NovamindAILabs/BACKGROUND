import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from remover import remove_bg

BASE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE, "static", "uploads")
OUTPUT_DIR = os.path.join(BASE, "static", "outputs")
ALLOWED = {"png", "jpg", "jpeg", "webp"}

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

def ok(name): return "." in name and name.rsplit(".",1)[1].lower() in ALLOWED

@app.get("/")
def index(): return render_template("index.html")

@app.post("/remove")
def remove():
    f = request.files.get("file")
    if not f or not ok(f.filename): return jsonify({"error":"invalid file"}), 400
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    in_name = secure_filename(f"{ts}_{f.filename}")
    in_path = os.path.join(UPLOAD_DIR, in_name); f.save(in_path)
    out_name = in_name.rsplit(".",1)[0] + ".png"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    try:
        remove_bg(in_path, out_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"output": f"/static/outputs/{out_name}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
