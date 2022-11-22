# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            if not(x or y or z) == (not x) and not(x or y or z) == (not y) and not(x or y or z) == (not z) :
                print(f"Утверждение истинно для X = {x}, Y = {y}, Z = {z}")
