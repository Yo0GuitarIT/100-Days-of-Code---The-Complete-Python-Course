from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def enter():
	page = ''
	return page
	
'''
@app.route('/<pageNumber>')
def index(pageNumber):
  return f"This is page {pageNumber}"
'''

randomText = ["Is's easy!!!",
							"Something tough~",
							"It took me a lot of time @@"]

@app.route('/<pageNumber>')
def index(pageNumber):
	link = f"https://replit.com/@justrockaoi/Day{pageNumber}100Days#main.py"
	page = ''
	f = open("temp/page.html","r")
	page = f.read()
	f.close()
	page = page.replace("{num}",pageNumber)
	page = page.replace("{link}",link)
	page = page.replace("{text}",random.choice(randomText))
	return page
  
app.run(host='0.0.0.0', port=81)
