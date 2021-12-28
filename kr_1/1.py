x = int(input())
maxi = 0
secondM = 0
counter = 1
while x != 0:
    if maxi < x:
        maxi = x
        secondM = 0
    elif maxi == x and secondM == 0:
        secondM = counter
    x = int(input())
    counter += 1
print(maxi, secondM)
