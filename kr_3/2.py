# В БИНАРНОМ ФАЙЛЕ numbers.bin записана последовательность целых 8 байтных чисел
# тип лонг лонг требуеттся отсортировать выбором и вывести это
import struct
from random import randint

n = 1000
f = open('numbers.bin', 'w')
f = open('numbers.bin', 'r+b')
f1 = open('numbers1.bin', 'w')
f1 = open('numbers1.bin', 'r+b')
for i in range(n):
    rand = randint(-1000, 1000)
    f.write(struct.pack('q', rand))
    f1.write(struct.pack('q', rand))


def show_file(base):
    s = []
    base.seek(0, 0)
    for i in range(n):
        a = base.read(8)
        a = struct.unpack('q', a)
        s += a
    print(s)


print("file before buble sort sort: ")
show_file(f)
print("file before selection sort sort: ")
show_file(f1)
print()

size = f.tell()
f.seek(0, 0)

for i in range(size // 8 - 1):
    for j in range(size // 8 - i - 1):
        f.seek(8 * j)
        a = f.read(8)
        b = f.read(8)
        f.seek(8 * j)
        if struct.unpack('q', a)[0] >= struct.unpack('q', b)[0]:
            f.seek(8 * j)
            f.write(b)
            f.write(a)


f1.seek(0)
for i in range(size // 8):
    for j in range(i+1, size // 8):
        f1.seek(i * 8)
        a1 = f1.read(8)
        f1.seek(8*j)
        b1 = f1.read(8)
        if struct.unpack('q', a1)[0] >= struct.unpack('q', b1)[0]:
            f1.seek(8 * j)
            f1.write(a1)
            f1.seek(i*8)
            f1.write(b1)



print("file after buble sort sort: ")
show_file(f)
print("file after selection sort sort: ")
show_file(f1)
