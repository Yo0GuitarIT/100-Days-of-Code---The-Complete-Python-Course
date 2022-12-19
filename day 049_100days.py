import time
f = open("high.score", "r")
list = []
add = []
numlist = []
dic ={}
big = []

while True:
	contents = f.readline().strip()
	if contents =="":
		break
	print(contents)
	str = contents
	add = str.split()
	list.append(add)		
f.close()	

for i in range(len(list)):
 	numlist.append(int(list[i][1]))

for i in range(len(list)):
	dic[list[i][0]] = numlist[i]

num = 0
for key,value in dic.items():
	if value > num:
		num = value
		big = [key,value]

print("\nCurrent Leader\n")
print("Analyzing high scores......\n")
time.sleep(1)
print(f"Current leader is {big[0]} {big[1]}")
