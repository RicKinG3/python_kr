m = int(input())
x = 0
z = 0
n = 0
t = 1
o = 0
while t != 0:
    t = int(input())
    if t > m:
        m = t
        z += 1 
        if z == 2:
            n = m
            o = x
    x += 1
if n == m:
    print(m, o+2)
print(n, o+2)
    
