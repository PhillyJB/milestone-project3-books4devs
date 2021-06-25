import os
from flask import Flask, render_template

app = Flask(__name__)

#routes and views for the html templates.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/glossary")
def glossary():
    return render_template("glossary.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=os.environ.get("PORT", "5000"), 
        debug=True)