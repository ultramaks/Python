#numbers = [1, -2, 3, 4, -5, 6, -7, -8, 9, 0]
numbers = [-1, 2, 3, 0]
changes = 0
pos = 0

for number in (len(numbers)):
    print ("Сравниваем " + str(numbers[pos]) +" с " + str(numbers[pos + 1]))
    if numbers[pos] > 0 and numbers[pos + 1] < 0 or numbers[pos] < 0 and numbers[pos + 1] > 0:
        changes += 1
        print ("Проход - " + str(pos) + ". Изменено - " + str(pos) + "\n")
        pos += 1

print("Число изменений знака в списке - " + str(changes))
