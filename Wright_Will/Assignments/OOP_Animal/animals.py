

create animal class
    name ---
    health 100
    walk() --health -=1
    run() -- health -= 5
    displayHealth()

instance of animal  --animal
    walk 3 times
    run 2 times
    displayHealth

create dog class
    super ??
    health = 150
    pet() -- health += 5
instance of dog
    walk() 3 times
    run()  2 times
    pet()
    displayHealth()
create dragon class
    health 170
    fly() health -= 10
    dispayHealth works a little differntly??
instance of dragon
    walk() 3 times
    run()  2 times
    fly()  2 times
    displayHealth()

instance of animal
    call fly() --shouldn't work
    call pet() -- shouldn't work




class animal(object):
