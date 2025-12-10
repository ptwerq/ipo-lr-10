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