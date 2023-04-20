from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']

@app.route('/')
def index():
	if session.get("loggedIn"):
		return redirect("/welcome")
	
	page = ""
	f = open("index.html", "r")
	page += f.read()
	f.close()
	return page

@app.route('/signup')
def signUp():
	page = ""
	f = open("signUp.html", "r")
	page += f.read()
	f.close()
	return page

@app.route('/signupstep',methods=["POST"])
def signUpStep():
	form = request.form
	db[request.form["username"]]={"name":request.form["name"],"password":request.form["password"]}
	return redirect("/")

@app.route('/login')
def login():
  page = ""
  f = open("login.html", "r")
  page += f.read()
  f.close()
  return page

@app.route('/loginStep',methods=["POST"])
def loginStep():
	form = request.form
	print(db[request.form["username"]]["password"])
	print(request.form["password"])
	try:
		if db[request.form["username"]]["password"]== request.form["password"]:
			session["loggedIn"] = form["username"]
			return redirect("/welcome") 
		else:
			return redirect("/login")
	
	except:
			return redirect("/login")

@app.route('/welcome')
def welcome():
  page = f"""<h1>Hi there {db[session["loggedIn"]]["name"]}</h1>
	<button type="button" onClick="location.href='/logout'">Logout</button>"""
  return page

@app.route('/logout')
def logout():
	session.clear()
	return redirect("/")

app.run(host='0.0.0.0', port=81)
