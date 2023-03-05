from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
	form = request.form
		
	if form["username"] == "aaa" and form["email"] == "a@a.com" and form["password"] == "111":
		return "You are logged in"
	elif form["username"] == "bbb" and form["email"] == "b@b.com" and form["password"] == "222":
		return "You are logged in"
	elif form["username"] == "ccc" and form["email"] == "c@c.com" and form["password"] == "333":
		return "You are logged in"
	else:
		return "Username, E-mail or password incorrect"



@app.route('/')
def index():
	page = ""
	f = open("static/index.html","r")
	page = f.read()
	f.close()
	return page
  
app.run(host='0.0.0.0', port=81)
