# Исходный файл int.txt записан текст отрывок из литер произведения.
# Текст содержит 5-10 предложений записан в 5-10 строк так, что ни одна строка кроме
# последней не оканчивается точкой. Написать прогу создающию новый файл out.tx,
# в которой В первой строке самое короткое предложение и во 2 самое длиное
f1 = open('out.txt', 'w+')
a = ''
count = 2
count_mas = []
count_pos = 0
count_pos_mas = []

with open('in.txt') as f:
    for i in f:
        count_pos += 1
        for j in i:
            count_pos += 1
            if j == " ":
                count += 1
            if j == ".":
                count_mas.append(count)
                count_pos_mas.append(count_pos)
                count_pos = 0
                count = 0
    f.seek(0, 0)
    mini = min(count_mas)
    min_index = count_mas.index(min(count_mas))
    sum_end = 0
    sum_start = 0
    for i in range(min_index + 1):
        sum_end += count_pos_mas[i]
    for i in range(min_index):
        sum_start += count_pos_mas[i]
    f.seek(sum_start)
    f1.write(f.read(sum_end - sum_start))

    f.seek(0)
    maxi = max(count_mas)
    max_index = count_mas.index(max(count_mas))
    sum_end = 0
    sum_start = 0
    for i in range(max_index + 1):
        sum_end += count_pos_mas[i]

    for i in range(max_index):
        sum_start += count_pos_mas[i]

    f.seek(sum_start)
    f1_max = (f.read(sum_end - sum_start))
    f1.write('\n')
    f1_max_new = ''
    for i in f1_max:
        if i != '\n':
            f1_max_new+=i
    f1.write(f1_max_new)


