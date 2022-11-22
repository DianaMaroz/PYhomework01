# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            if not(x or y or z) == (not x) and not(x or y or z) == (not y) and not(x or y or z) == (not z) :
                print(f"Для X = {x}, Y = {y}, Z = {z} утверждение истинно")
            else:
                print(f"Для X = {x}, Y = {y}, Z = {z} утверждение ложно")
