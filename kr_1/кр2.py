import math as m
a = [int(input('эл')) for i in range(int(input()))]
b = [ ]
s = 0
k = 0
for i in range (len(a)):
    if a[i] > 0:
        b.append(a[i])
    if a[i] < 0:
        k = i
t = m.gcd(*b)        
print(t)
a[k] = t
print(*a)
