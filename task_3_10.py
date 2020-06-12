import random

values = []

size = int(input("Введите размер списка:\n"))

for i in range(size):
    x = random.randint(0, 99)
    values.append(x)

print("Список - " + str(values))

sum = values[-1] + values[-2] + values[-3]
sr_ar = sum/3

print ("Сумма трех последних чисел = " + str(sum))
print ("Среднее арифметическое = " + str(sr_ar))