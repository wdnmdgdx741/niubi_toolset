# coding: utf-8
from flask import Flask


app = Flask(__name__)


@app.route("/index")
def inde():
    return "heeello world"


if __name__ == "__main__":
    app.run()