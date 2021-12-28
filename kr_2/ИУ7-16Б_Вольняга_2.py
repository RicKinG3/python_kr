
#III.  Задача 2. Задана символьная матрица. Создать вектор, в который записать среднее
# арифметическое числовых элементов каждого столбца, в котором есть цифры.
n = int(input('введите кол-во строк'))
m = int(input('введите кол-во столбцов'))
a = [ ]
for i in range(n):
    a.append([ ])
    for j in range(m):
        a[i].append(input('ВВедите элемент '))
av = [ ]
for i in range(m):
    k = 0
    s = 0
    for j in range(n):
        if a[j][i].isdigit():
            s+=int(a[j][i])
            k+=1
        if k!=0:
            av.append(s/k)
        else:
            av.append('нет цифр')

for i in a:
    print(*i)
print()
for i in range(n):
    for j in range(m):
        for k in a[i][j]:
            if k in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                for x in range(m):
                    a[i][x] = '#'
                for x in range(n):
                    a[x][j] = '#'
for i in a:
    print(*i)
print()
print(*av)
