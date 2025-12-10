from collision import (
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect
)

# 1. Проверка корректности прямоугольника
rect1 = [(0, 0), (5, 5)]
print("Корректность rect1:", isCorrectRect(rect1))

# 2. Проверка пересечения прямоугольников
rect2 = [(-2, -2), (3, 3)]
print("Пересекаются rect1 и rect2:", isCollisionRect(rect1, rect2))

# 3. Площадь пересечения двух прямоугольников
rect3 = [(2, 2), (7, 8)]
print("Площадь пересечения rect1 и rect3:", intersectionAreaRect(rect1, rect3))

# 4. Площадь пересечения множества прямоугольников
rectangles = [
    [(0, 0), (5, 5)],
    [(-2, -2), (3, 3)],
    [(1, 1), (6, 6)],
    [(4, 4), (10, 10)]
]

print("Уникальная площадь пересечения множества:", intersectionAreaMultiRect(rectangles))