print "get a number sqrt "
while True:
    x = float(raw_input("enter a number :"))
    low = 0
    high = x
    guess = (low + high) / 2

    while abs(guess ** 2 - x) > 1e-5:
        if guess ** 2 > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
        
    print guess
    cancel = raw_input("continue?(enter\q)")
    if cancel == "q":
        print "byebye!"
        break

