# -*- coding: utf-8 -*-

n, m = (int(i) for i in input().split())
a = [[int(i) for i in input().split()] for _ in range(n)]
print(a)

max_elem = a[0][0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]

list_index_max = [(i, j) for i in range(len(a)) for j in range(len(a[i])) if a[i][j] == max_elem]
line, column = list_index_max[0]
print('максимальный элемент = ', max_elem)
print('строка =', line, 'столбец =', column)
rule_add = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

rule_div = {
    ('I', 'V'): 3,
    ('I', 'X'): 8,
    ('X', 'L'): 30,
    ('X', 'C'): 80,
    ('C', 'D'): 300,
    ('C', 'M'): 800,
}

def roman_to_arabic(roman_number):
    number = 0
    prev_literal = None
    for literal in roman_number:
        if prev_literal and rule_add[prev_literal] < rule_add[literal]:
            number += rule_div[(prev_literal, literal)]
        else:
            number += rule_add[literal]
        prev_literal = literal
    return number

