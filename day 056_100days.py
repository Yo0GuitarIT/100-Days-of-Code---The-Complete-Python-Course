import csv, os
fileExist = True

art = {}

with open("100MostStreamedSongs.csv") as file:
	reader = csv.DictReader(file)
	
	for row in reader:
		Artists = row["Artist(s)"]
		Song = row["Song"]
		try:
			os.mkdir(Artists)
		except:
			pass
    
		path = f"{Artists}/{Song}.txt"
		f = open(path, "w")
		f.close()
