from collision.rect import isCorrectRect, isCollisionRect, RectCorrectError

try:
    print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))  # True
except RectCorrectError as e:
    print(e)

try:
    print(isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]))  # False
except RectCorrectError as e:
    print(e)

try:
    print(isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]))  # Ошибка
except RectCorrectError as e:
    print(e)