from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
		 os.system("clear")
		 print("let's Play~~")
		 print("Press 1 to Stop")
		 i = int(input())
		 if i == 1:
			 os.system("clear")
			 source.paused = True
			 print("stop")
			 print("Press 1 to Play")
			 #i = int(input())
			 return
		 else:
			 continue
  
while True:
  os.system("clear")
  print("🎵 MyPOD Music Player")
  print("Press 1 to Play")
  print("Press 2 to Exit")
  i = int(input())
  if i == 1:
   play()
  elif i == 2:
	  print("Bye")
	  break
  else:
	  print("Press anything else to see the menu again.")
	  time.sleep(1)
