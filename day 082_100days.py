from flask import Flask, request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def lang():
  data = request.args
  if data == {}:
    return "Nothing here"
  if data["lang"]=="eng":
    return "Hello, and welcome to our website~"
  if data["lang"]=="cn":
    return "ni hao, ~"
@app.route('/')
def index():
	return "Hello from Flask"


app.run(host='0.0.0.0', port=81)
