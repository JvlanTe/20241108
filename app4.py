from flask import Flask, render_template, request, redirect, url_for, flash
import secrets
import os

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/", methods=["GET"])
def index():
    return render_template("image.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません")
            return redirect(url_for("index"))

        file = request.files["file"]

        if file.filename == "":
            flash("ファイルが選択されていません")
            return redirect(url_for("index"))

        if file:
            file_path = os.path.join("static", "images", file.filename)
            file.save(file_path)

            flash("ファイルが正常にアップロードされました")
            return render_template("upload.html", filename=file.filename)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
