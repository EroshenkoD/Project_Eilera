"""
Основными факторами 13195 являются 5, 7, 13 и 29.
Что является самым большим основным фактором числа 600851475143?

"""
a = 600851475143
osn_factor = []
i = 2

while i <= a:
    if not a % i:
        osn_factor.append(i)
        a = a // i
        i = 2
        continue
    i += 1


print(max(osn_factor))
