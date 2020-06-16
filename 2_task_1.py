print("Введите стороны прямоугольника a и b:")
a = int(input("a = "))
b = int(input("b = "))
print("Прямоугольник со сторонами: a = " + str(a) + " и b = " + str(b))


def find_squares(a, b):
    result = []
    while (a > 0):
        if a < b:
            a, b = b, a
        result.append(b)
        a -= b
        find_squares(a, b)
    return result

print("\nПолучено квадратов: " + str(len(find_squares(a, b))) + ". Стороны квадратов: " + str(find_squares(a, b)))