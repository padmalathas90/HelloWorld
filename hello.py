from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<username>")
def greet(name):
    return f"Hello there { name}!"

if __name__ == "__main__":
    app.run(debug=True)
