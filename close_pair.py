import math
from typing import Optional

def closest_pair_recursive(points_x: list[tuple[float, float]], points_y: list[tuple[float, float]]) -> tuple[float, tuple[float, float], tuple[float, float]]:
    """Рекурсивная функция для поиска ближайшей пары точек."""
    n = len(points_x)
    if n <= 3:  # Базовый случай: перебор для небольшого количества точек
        return base_force_closest_pair(points_x)

    mid_x = points_x[n // 2][0]
    points_left_x = points_x[:n // 2]
    points_right_x = points_x[n // 2:]

    points_left_y = []
    points_right_y = []
    for point in points_y:
        if point[0] <= mid_x:
            points_left_y.append(point)
        else:
            points_right_y.append(point)

    closest_left = closest_pair_recursive(points_left_x, points_left_y)
    closest_right = closest_pair_recursive(points_right_x, points_right_y)

    min_distance = min(closest_left[0], closest_right[0])
    closest_pair = closest_left if closest_left[0] < closest_right[0] else closest_right

    strip = []
    for point in points_y:
        if abs(point[0] - mid_x) < min_distance:
            strip.append(point)

    closest_strip = closest_pair_in_strip(strip, min_distance)

    if closest_strip[0] < min_distance:
        closest_pair = closest_strip

    return closest_pair


def closest_pair_in_strip(strip: list[tuple[float, float]], min_distance: float) -> tuple[float, tuple[float, float], tuple[float, float]]:
    """Находит ближайшую пару в полосе."""
    min_dist_strip = min_distance
    closest_pair_strip = (min_distance, (0, 0), (0, 0))
    strip.sort(key=lambda point: point[1])  # Сортировка по y-координате
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist_strip:
                break
            dist = math.dist(strip[i], strip[j])
            if dist < min_dist_strip:
                min_dist_strip = dist
                closest_pair_strip = (dist, strip[i], strip[j])
    return closest_pair_strip


def base_force_closest_pair(points: list[tuple[float, float]]) -> tuple[float, tuple[float, float], tuple[float, float]]:
    """Базовый случай: перебор для небольшого количества точек."""
    min_distance = float('inf')
    closest_pair = (min_distance, (0, 0), (0, 0))
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = math.dist(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (min_distance, points[i], points[j])
    return closest_pair


def closest_pair_of_points(points: list[tuple[float, float]]) -> Optional[tuple[float, tuple[float, float], tuple[float, float]]]:
    """Функция для запуска рекурсивного алгоритма."""
    if len(points) < 2:
        return None
    points_x = sorted(points, key=lambda point: point[0])
    points_y = sorted(points, key=lambda point: point[1])
    return closest_pair_recursive(points_x, points_y)

# Примеры использования


assert closest_pair_of_points([(1, 1), (2, 2), (1, 2)]) == (1, (1, 1), (1, 2))

print(closest_pair_of_points([(1, 1), (9, 9), (9, 12)]))
