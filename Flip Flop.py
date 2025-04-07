def flip_flop(r):
    e = len(r) - 1
    s = 0

    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True

t = (1,2,3,3,2,1)

if (flip_flop(t)):
    print("the tuple is flip flop")

else:
    print("the tuple is not flip flop")