from flask import Flask ,request
import datetime

app = Flask(__name__)

@app.route('/hello', methods = ["GET"])
def hello():
	data = request.args
	temp = "default"
	if data != {}:
		temp = data["temp"]

	today = f"{datetime.date.today()}"
	page = ""
	f = open("index.html","r")
	page = f.read()
	page = page.replace("{date}",today)
	page = page.replace("{temp}",temp)
	f.close()
	return page

@app.route('/')
def index():
	return "hi"

app.run(host='0.0.0.0', port=81)
