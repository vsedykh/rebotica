def haw_even(weqa):
    wasd = 0
    for rty in weqa:
        if rty%2==1:
            wasd+=1
    return wasd
tre = [12, 54, 765, 354, 22, 433, 678, 854, 56, 211, 11, 101, 69]
print(haw_even(tre))