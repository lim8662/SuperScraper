from flask import Flask

app = Flask("SuperScraper")

@app.route("/")
def home():
  return "<h1"

@app.route("/<name>/")
def contact(name):
  return f"hello {name}!"
app.run(host="0.0.0.0")
