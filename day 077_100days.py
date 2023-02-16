from flask import Flask,redirect
import datetime


app = Flask(__name__)

@app.route('/')
def aaa():
	page = ""
	return page

@app.route('/yo0')
def Yo0():
	return redirect("https://www.instagram.com/yo0_36563/")
  
											

@app.route('/hello')
def hello():
	today = f"{datetime.date.today()}"
	page = ""
	f = open("template/portfolio.html","r")
	page = f.read()
	page = page.replace("{step}","Hello")
	page = page.replace("{date}",today)
	page = page.replace("{link}","https://www.facebook.com/memento.mori1927")
	return page

@app.route('/bye')
def index():
	today = f"{datetime.date.today()}"
	page = ""
	f = open("template/portfolio.html","r")
	page = f.read()
	page = page.replace("{step}","Bye")
	page = page.replace("{date}",today)
	page = page.replace("{link}","https://www.facebook.com/memento.mori1927")
	return page
	
app.run(host='0.0.0.0', port=81)
