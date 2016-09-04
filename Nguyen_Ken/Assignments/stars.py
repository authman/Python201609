#draw stars

# draw_stars()

ken = [1,2,3,4,10,8,"ken",20,10,8]
jessica = ["philpot","peanut","banana","glove","dance"]
bryan = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]

def stars(b):
    stars = "*"
    stars *= b
    return stars

def stringStars(c):
    strings = ""
    stringLength = len(c)
    strings = c[0]*stringLength
    return strings

def draw_stars(a):
    for i in range(len(a)):
        if (type(a[i]) is str):
            c = a[i].lower()
            print stringStars(c)

        elif (type(a[i]) is int):
            print stars(a[i])

draw_stars(bryan*15)
