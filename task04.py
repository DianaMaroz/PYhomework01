# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)
try:

    quater_num = int(input("Укажите номер четверти"))
    if quater_num == 1:
        print("Диапазон возможных координат точек: х > 0, y > 0")
    elif quater_num == 2:
        print("Диапазон возможных координат точек: х < 0, y > 0")
    elif quater_num == 3:
        print("Диапазон возможных координат точек: х < 0, y > 0")
    elif quater_num == 4:
        print("Диапазон возможных координат точек: х > 0, y < 0")
    else:
        print("Введено некорректное значение")
except:
    print("Введено некорректное значение")
