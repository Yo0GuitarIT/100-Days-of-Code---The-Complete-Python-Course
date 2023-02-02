import tkinter as tk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x300")
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
		canvas.pack_forget()
		errorLabel.pack()
		return
	errorLabel.pack_forget()
	canvas.pack()

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
container = canvas.create_image(200,0,image = None)

errorLabel = tk.Label(text = "Unable to find this user")


window.mainloop()
