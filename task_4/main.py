from collision.rect import intersectionAreaRect, isCorrectRect

try:
    area = intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])
    print("Площадь пересечения:", area)  # >0
except ValueError as e:
    print(e)

try:
    area = intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)])
    print("Площадь пересечения:", area)  # 0
except ValueError as e:
    print(e)

try:
    area = intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])
    print("Площадь пересечения:", area)
except ValueError as e:
    print(e)  # "2й прямоугольник некорректный"