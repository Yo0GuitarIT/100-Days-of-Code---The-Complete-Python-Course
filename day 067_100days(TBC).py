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
window.geometry("300x300")

firstlabel = tk.Label(text = "Guess Who?")
firstlabel.pack()

a = tk.StringVar()
a.set('')

def show():
	name = a.get()
	print(name)
	a.set('')
	
def changeImage():
	canvas.itemconfig(container, image = kate)

wordentry = tk.Entry(window, textvariable = a)
wordentry.pack()

btn = tk.Button(text="Find",command = changeImage)
btn.pack()

canvas = tk.Canvas(window,width=300,heigh = 300)
canvas.pack()

charlotte = tk.PhotoImage(file = "charlotte.png")
charlotte = charlotte.subsample(4)
gerald = tk.PhotoImage(file = "gerald.png")
gerald = gerald.subsample(4)
mo = tk.PhotoImage(file = "mo.png")
mo = mo.subsample(4)
kate = tk.PhotoImage(file = "katie.png")
kate = kate.subsample(4)

container = canvas.create_image(150,0, image = mo)


window.mainloop()
