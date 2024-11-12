from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        message = request.form["message"]
        return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
