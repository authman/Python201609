def draw_stars(something):
	for element in something:
		print "*" * element

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)





def draw_stars_2(something):
	for element in something:
		if not type(element) is str:
			print "*" * element
		else:
			print element[0].lower() * len(element)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_2(x)
			
