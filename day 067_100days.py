import tkinter as tk

'''
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
	canvas.itemconfig(container, image = newImage)
	
hello = tk.Label(text="Hello World!")
hello.pack()
button = tk.Button(text = "Click me!",command=changeImage)
button.pack()
canvas = tk.Canvas(window,width=560,heigh = 537)
canvas.pack()
image = tk.PhotoImage(file = "theFeels.png")
newImage = tk.PhotoImage(file = "flower.png")
image = image.subsample(4)
newImage = newImage.subsample(10)
container = canvas.create_image(150,50,image = image)

tk.mainloop()
'''

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x200")
label = "Guess Who?"

def imageShow():
	person = text.get("1.0","end")
	if person.lower().strip() == "mo":
		canvas.itemconfig(container, image = mo)
	elif person.lower().strip() == "katie":
		canvas.itemconfig(container, image = katie)
	elif person.lower().strip() == "gerald":
		canvas.itemconfig(container, image = gerald)
	elif person.lower().strip() == "charlotte":
		canvas.itemconfig(container, image = charlotte)
	else:
		firstlabel["text"] = "Unable to find user."

firstlabel = tk.Label(text = label)
firstlabel.pack()
text = tk.Text(window,height=1,width=30)
text.pack()
button = tk.Button(text="Find",command = imageShow)
button.pack()
canvas = tk.Canvas(window,height=400,width=180)
canvas.pack()
charlotte = tk.PhotoImage(file = "charlotte.png")
gerald = tk.PhotoImage(file = "gerald.png")
katie = tk.PhotoImage(file = "katie.png")
mo = tk.PhotoImage(file = "mo.png")

container = canvas.create_image(200,0,image = mo)

window.mainloop()
