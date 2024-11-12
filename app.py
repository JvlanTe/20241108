from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello Flask!"


# @app.route("/user/<name>")
# def user(name):
#     return f"こんにちは、{name}!"


@app.route("/user/<name>")
def usert(name):
    return render_template("user.html", name=name)


@app.route("/fruits")
def frutis():
    fruits = ["りんご", "バナナ", "オレンジ", "いちご", "ぶどう"]
    return render_template("fruits.html", fruits=fruits)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
