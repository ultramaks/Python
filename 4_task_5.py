# Номер строки с которой начинаем копировать
string = 4
offset = 0

with open("F1.txt", "r") as F1:
    with open("F2.txt", "w") as F2:
        for line in F1:
            offset += 1
            if offset > int(3):
                F2.write(line)

F1.close()
F2.close()

with open('F2.txt', 'r') as file:
    data = file.read().replace('\n', '')

for line in data:
    words = data.split()
file.close()

print("В последнем слове файла F2 всего " +(str(len(words[-1]))) + " символов")