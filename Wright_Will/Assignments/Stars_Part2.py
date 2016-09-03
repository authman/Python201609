
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(lst):
    for n in lst:
        if type(n) ==type(1):
            print("*"*n)
        else:
            print n[0].lower()*len(n)

draw_stars(x)
