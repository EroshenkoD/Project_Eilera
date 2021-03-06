"""
Последовательность номеров треугольников генерируется путем сложения натуральных чисел. Таким образом, номер 7- го
треугольника будет 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять слагаемых будут:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим факторы первых семи треугольных чисел:

 1 : 1
 3 : 1,3
 6 : 1,2,3,6
10 : 1,2,5,10
15 : 1,3,5,15
21 : 1,3,7,21
28 : 1,2, 4,7,14,28
Мы можем видеть, что 28 - это первое число треугольника, имеющее более пяти делителей.

Каково значение первого треугольного числа, имеющего более пятисот делителей?
"""


b = 0

for a in range(1, 100):
    b += a
print(b)

i = 0
list_del = []

while i <= b//2:
    i += 1
    print(i)
    if not b % i:
        list_del.append(i)
        
list_del.append(b)
print(len(list_del))
