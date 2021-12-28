
t = int(input())
z = 1
if t % 2 != 0 or t<=127: 
    exit(0)
for i in range(1, 128, 2):
    z *= (t-i-1)/(t-i)
print(z)   

