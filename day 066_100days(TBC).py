import tkinter as tk

labal = 0
def bottonChoice(i):
	global labal
	labal = f"{labal}{i}"
	labal = int(labal)
	result["text"] = labal


def typeAns(operator):
	global labal,lastNum,op
	if operator == "+":
		op = "+"
	elif operator =="-":
		op = "-"
	elif operator =="*":
		op = "*"
	else: #"/"
		op = "/"
	lastNum = labal
	labal = 0
	result["text"] = labal
	
def equal():
	global labal,lastNum,op
	if op == "+":
		labal = lastNum+labal
	elif op =="-":
		labal = lastNum-labal
	elif op =="*":
		labal = lastNum*labal
	else:
		labal = lastNum/labal
		
	result["text"] = labal
	
def clear():
	global labal,lastNum
	labal = 0
	lastNum = 0
	result["text"] = labal

window = tk.Tk()
window.title("Calculator") 
window.geometry("200x200") 

result = tk.Label(text = labal)
result.grid(row=0,column = 1)

btn1 = tk.Button(text = "1",command = lambda:bottonChoice(1)) 
btn1.grid(row=1, column = 0)
btn2 = tk.Button(text = "2",command = lambda:bottonChoice(2)) 
btn2.grid(row=1, column = 1)
btn3 = tk.Button(text = "3",command = lambda:bottonChoice(3)) 
btn3.grid(row=1, column = 2)
btn4 = tk.Button(text = "4",command = lambda:bottonChoice(4)) 
btn4.grid(row=2, column = 0)
btn5 = tk.Button(text = "5",command = lambda:bottonChoice(5)) 
btn5.grid(row=2, column = 1)
btn6 = tk.Button(text = "6",command = lambda:bottonChoice(6)) 
btn6.grid(row=2, column = 2)
btn7 = tk.Button(text = "7",command = lambda:bottonChoice(7)) 
btn7.grid(row=3, column = 0)
btn8 = tk.Button(text = "8",command = lambda:bottonChoice(8)) 
btn8.grid(row=3, column = 1)
btn9 = tk.Button(text = "9",command = lambda:bottonChoice(9)) 
btn9.grid(row=3, column = 2)
btn0 = tk.Button(text = "0",command = lambda:bottonChoice(0))
btn0.grid(row=4, column = 1)

addition = tk.Button(text="+",command = lambda:typeAns("+"))
addition.grid(row=1, column=3)
subtraction = tk.Button(text = "-",command = lambda:typeAns("-"))
subtraction.grid(row=1, column=4)
multiplication = tk.Button(text = "*",command = lambda:typeAns("*"))
multiplication.grid(row=2, column=3)
division = tk.Button(text = "/",command = lambda:typeAns("/"))
division.grid(row=2, column=4)
equaltion = tk.Button(text = "=",command = lambda:equal())
equaltion.grid(row=4, column=3)
btnClear = tk.Button(text = "c",command = lambda:clear())
btnClear.grid(row=4, column=4)

tk.mainloop()
