"""
Сумма простых чисел ниже 10 составляет 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел ниже двух миллионов.

"""

all_sum = 0
a = 2
list_n = []
b = 0
while True:
    if not len(list_n):
        list_n = [i for i in range(2, 2000000) if i % a]
    else:
        b = len(list_n)
        list_n = [i for i in list_n if i % a]
    all_sum += a
    if not len(list_n):
        break
    a = list_n[0]
    if b - len(list_n) == 1:
        break

for i in list_n:
    all_sum += i

print(all_sum)