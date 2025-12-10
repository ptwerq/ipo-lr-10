from collision.rect import intersectionAreaMultiRect, RectCorrectError

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

try:
    result = intersectionAreaMultiRect(rectangles)
    print(f"Уникальная площадь пересечения: {result}")
except RectCorrectError as e:
    print(e)

# Некорректный прямоугольник
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]  # Некорректный прямоугольник
]

try:
    intersectionAreaMultiRect(incorrect_rectangles)
except RectCorrectError as e:
    print(e)  # "2й прямоугольник некорректный"