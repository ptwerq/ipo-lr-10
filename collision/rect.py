def isCorrectRect(points):
    """
    Проверяет корректность прямоугольника, заданного списком из двух кортежей:
    [ (x1, y1), (x2, y2) ]

    Возвращает True если корректно, иначе False.
    """
    # Должно быть ровно 2 точки в списке
    if not isinstance(points, list) or len(points) != 2:
        return False

    p1, p2 = points

    # Каждая точка — кортеж из 2 элементов
    if not (isinstance(p1, tuple) and isinstance(p2, tuple)):
        return False
    if not (len(p1) == 2 and len(p2) == 2):
        return False

    x1, y1 = p1
    x2, y2 = p2

    # Координаты должны быть числами (int или float)
    for v in (x1, y1, x2, y2):
        if not isinstance(v, (int, float)):
            return False

    # x1 < x2 и y1 < y2
    return x1 < x2 and y1 < y2



# кастомная ошибка для некорректного прямоугольника
class RectCorrectError(Exception):
    pass

# проверка корректности прямоугольника
def isCorrectRect(rect):
    if len(rect) != 2:
        return False
    (x1, y1), (x2, y2) = rect
    return x1 < x2 and y1 < y2

# проверка пересечения двух прямоугольников
def isCollisionRect(rect1, rect2):
    # проверяем первый прямоугольник
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    # проверяем второй прямоугольник
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")

    x1_min, y1_min = rect1[0]
    x1_max, y1_max = rect1[1]
    x2_min, y2_min = rect2[0]
    x2_max, y2_max = rect2[1]

    # проверка пересечения по осям
    intersect_x = not (x1_max < x2_min or x2_max < x1_min)
    intersect_y = not (y1_max < y2_min or y2_max < y1_min)

    return intersect_x and intersect_y



def intersectionAreaRect(rect1, rect2):
    """
    Вычисляет площадь пересечения двух прямоугольников.
    rect1, rect2: списки из двух кортежей [(x1,y1),(x2,y2)]
    
    Возвращает:
        float — площадь пересечения.
        0 — если прямоугольники не пересекаются.
    
    Вызывает ValueError, если один из прямоугольников некорректный.
    """
    # Проверяем корректность прямоугольников
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некорректный")
    
    # Распаковываем координаты
    x1_min, y1_min = rect1[0]
    x1_max, y1_max = rect1[1]
    x2_min, y2_min = rect2[0]
    x2_max, y2_max = rect2[1]

    # Находим координаты пересечения
    x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min))
    y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min))

    # Площадь пересечения
    return x_overlap * y_overlap