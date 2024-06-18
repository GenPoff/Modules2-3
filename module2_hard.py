import time

stone1 = int(input('Какое число выпало на первом камне от 3 до 20? Введи его: '))
print('Вычисляю пароль для второго камня...')
time.sleep(3)
result = []
for i in range(1, 21):
    for j in range(2, 21):
        if stone1 % (i + j) == 0 and i < j:
            result.append(i)
            result.append(j)
        else:
            j += 1

print('А вот и пароль: ', result)

