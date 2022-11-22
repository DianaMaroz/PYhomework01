# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3


try:
    x_user = int(input("Введите координату х"))
    y_user = int(input("Введите координату y"))
    def define_quater(x, y):

        if x > 0 and y > 0:
            quater = 1
        elif x < 0 and y > 0:
            quater = 2
        elif x < 0 and y < 0:
            quater = 3
        elif x > 0 and y < 0:
            quater = 4
        return quater

    quater_user = define_quater(x_user, y_user)
    print(f"Точка с координатами ({x_user}, {y_user}) расположена в  {quater_user} четверти")
except:
    print("Данные введены не корректно")