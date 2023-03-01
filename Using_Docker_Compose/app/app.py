from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    path = "./textfile.txt"  # path inside container
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
    else:
        content = "File not found!"
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
