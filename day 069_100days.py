import tkinter as tk

def changeSence():
	canvas.itemconfig(container, image = apple)
	text3.pack_forget()
	text5.pack_forget()
	text6.pack_forget()
	btn5.forget()
	text1.pack()
	btn1.pack()
	btn2.pack()
	
def changeSence1():
	canvas.itemconfig(container, image = gun)
	text1.pack_forget()
	btn1.forget()
	btn2.forget()
	text2.pack()
	btn3.pack()
	btn4.pack()

def changeSence2():
	canvas.itemconfig(container, image = king)
	text2.pack_forget()
	btn3.forget()
	btn4.forget()
	text3.pack()
	btn5.pack()

def changeSence3():
	canvas.itemconfig(container, image = fairy)
	text1.pack_forget()
	btn1.forget()
	btn2.forget()
	text4.pack()
	btn6.pack()
	btn7.pack()

def changeSence4():
	canvas.itemconfig(container, image = treasure)
	text2.pack_forget()
	btn3.forget()
	btn4.forget()
	text4.pack_forget()
	btn6.forget()
	btn7.forget()
	text5.pack()
	btn5.pack()

def changeSence5():
	canvas.itemconfig(container, image = death)
	text4.pack_forget()
	btn6.forget()
	btn7.forget()
	text6.pack()
	btn5.pack()
	
	
window = tk.Tk()
window.title("Visual Novel")
window.geometry("350x400")

canvas = tk.Canvas(window,height=200,width=300)
canvas.pack()

text1 = tk.Label(text = "You see an apple, what will you do?")
text2 = tk.Label(text = "You see a gun, what will you do?")
text3 = tk.Label(text = "You are a king~~~")
text4 = tk.Label(text = "You see a fairy, what will you do?")
text5 = tk.Label(text = "You got treasure ~~~")
text6 = tk.Label(text = "Death is comming...")
text1.pack()

#layer apple
btn1 = tk.Button(text = "pick it up",command = changeSence1)
btn1.pack()
btn2 = tk.Button(text = "throw it up",command = changeSence3)
btn2.pack()

#layer gun
btn3 = tk.Button(text = "shoot!!",command = changeSence2)
btn4 = tk.Button(text = "throw it up",command = changeSence4)

#layer fairy
btn6 = tk.Button(text = "Be a friendl",command = changeSence4)
btn7 = tk.Button(text = "Catch!!",command = changeSence5)

#layer restart
btn5 = tk.Button(text = "restart",command = changeSence)


apple = tk.PhotoImage(file = "apple.png")
apple = apple.subsample(3)
death = tk.PhotoImage(file = "death.png")
death = death.subsample(4)
fairy = tk.PhotoImage(file = "fairy.png")
fairy = fairy.subsample(3)
gun = tk.PhotoImage(file = "gun.png")
gun = gun.subsample(13)
king = tk.PhotoImage(file = "king.png")
king = king.subsample(6)
treasure = tk.PhotoImage(file = "treasure.png")
treasure = treasure.subsample(20)

container = canvas.create_image(150,100,image = apple)

window.mainloop()
