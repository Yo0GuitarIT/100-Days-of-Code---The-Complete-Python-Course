from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/portfolio') 
def portfolio(): 
  page = """
	<html>
<head>
	<title>My Portfolio</title>
  <link href="static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>
	<h1>Yo0 - Portfolio</h1>
	
	<h2>Wow, One Hundred Days?!</h2>
	<p>Let's start with some simple code to get a simple output (the information the program gives to the user).</p>
	<a href = "https://replit.com/@justrockaoi/day-1100-days#main.py"><img src="static/images/p1.png" width = 35%></a>
	
	<h2>Taking user input</h2>
	<p>Let's take a look at the input command and how that works. Input is when the user gives information to the computer.</p>
	<a href = "https://replit.com/@justrockaoi/day2100-days#main.py"><img src="static/images/p2.png" width = 35%></a>
	
	<h2>Concatenate</h2>
	<p>All it really means is combine text (remember, text is called a string) and variables together into single sentences! 😲🤯</p>
	<a href = "https://replit.com/@justrockaoi/day-3100-days#main.py"><img src="static/images/p3.png" width = 35%></a>
	
	<h2>Everyone loves a good story!</h2>
	<p>Well, you're going to create your own adventure story that places your user in the role of the main character and we'll even customize the story to suit their interests.</p>
	<a href = "https://replit.com/@justrockaoi/day4100-days#main.py"><img src="static/images/p4.png" width = 35%></a>
	
	<h2>If Statements</h2>
	<p>These statements are a bit like asking a question. You are telling the computer: if something is true, then do this specific block of code. Double equals (==) is asking the computer to compare if these two things are exactly the same.</p>
	<a href = "https://replit.com/@justrockaoi/day5100-days#main.py"><img src="static/images/p5.png" width = 35%></a>
	
</body>
</html>
  """
  return page


	
@app.route('/linktree') 
def linktree(): 
  page = """
	<html>
	<head>
		<title>Yo0' link tree</title>
		<link href="static/css/linktree.css" rel="stylesheet" type="text/css" />
	</head>
	<body>
		<img src="static/images/linkTree.png" width=50%>
		<h1>Yu Ling Chen</h1>
		<h2>Life is real. Life is earnest.</h2>
		<p>Socials</p>
		<ul class="list">
			<li><a href="https://www.facebook.com/memento.mori1927">Facebook(@memento.mori1927)</a></li>
			<li><a href="https://www.youtube.com/channel/UCqEEyVUmxX1z3b6QCPMzT8Q">Youtube(Chen Yu Ling)</a></li>
			<li><a href="https://replit.com/@justrockaoi">replit(@justrockaoi)</a></li>
		</ul>
	</body>
</html>
  """
  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
