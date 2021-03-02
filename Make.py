characters="abcdefghijklmnopqrstuvwxyz123456789"
for firstletter in characters:
	for secondletter in characters:
		for thirdletter in characters:
			print(f"{firstletter}{secondletter}{thirdletter}")
			f = open("usernames.txt","a")
			f.write(f"{firstletter}{secondletter}{thirdletter}\n")
			f.close()
