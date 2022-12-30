counter = 0

def tester(str,wordNum,counter): #(radar,5,0) #(radar,4,1)
	#print(f"{str[0+counter]}:{str[wordNum-1]}")
	if str[0+counter] != str[wordNum-1]:
		print(f"{str} is not palindrome. Oop!\n")
		return 
		
	if 0+counter == wordNum-1:
		print(f"{str} is a palindrome. Yay!\n")
		return 
	elif 0+counter+1 == wordNum-1:
		print(f"{str} is a palindrome. Yay!\n")
		return 
		
	else:
		tester(str,wordNum-1,counter+1)
		
while True:
	print("Palindrome Checker")
	word = input("Input a word > ").lower()
	wordNum = int(len(word))
	
	ans = tester(word,wordNum,counter)
  
