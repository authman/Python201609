def drawing_stars2(draw):
	for item in draw:
		if type(item) != str:
			print '*' * item
		else: 
			print str.lower (item[0])* len(item) 

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawing_stars2(x)