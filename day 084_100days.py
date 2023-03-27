from flask import Flask, request, redirect
from replit import db


app = Flask(__name__, static_url_path='/static')

@app.route('/loginPage')
def loginPage():
	page = ""
	f = open("loginPage.html", "r")
	page = f.read()
	f.close()
	return page

@app.route('/login', methods=["POST"])
def login():
  form = request.form
 
  try:
    if db[request.form["username"]]["password"]== request.form["password"]:
      return "hello~"+request.form["name"]
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")
	
@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""


@app.route("/changePass", methods=["POST"])
def change():
  form = request.form

  db[request.form["username"]] ["password"]= request.form["newPassword"]
  return f"""Password changed to {request.form['newPassword']}"""

@app.route("/signUpPage")
def signUpPage():
	page = ""
	f = open("signUpPage.html", "r")
	page = f.read()
	f.close()
	return page

@app.route("/signUp",methods=["POST"])
def signUp():
	form = request.form
	db[request.form["username"]] = {"name":request.form["name"],"password":request.form["password"]}

	return "Sign up~"

@app.route('/')
def index():
  page = ""
  f = open("index.html", "r")
  page = f.read()
  f.close()
  return page

app.run(host='0.0.0.0', port=81)
