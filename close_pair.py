from typing import Optional


def closest_pair_of_points(points: list[tuple[float, float]]) -> Optional[tuple[float, tuple[float, float], tuple[float, float]]]:
    """Находит ближайшую пару точек в массиве"""
    if len(points) < 2:
        return None

    min_distance: float = float('inf')
    closest_pair: Optional[tuple[float, tuple[float, float], tuple[float, float]]] = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = (sum((p_coord - q_coord) ** 2.0 for p_coord, q_coord in zip(points[i], points[j]))) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_pair = (min_distance, points[i], points[j])

    return closest_pair

# Примеры использования


assert closest_pair_of_points([(1, 1), (2, 2), (1, 2)]) == (1, (1, 1), (1, 2))

print(closest_pair_of_points([(1, 1), (9, 9), (9, 12)]))
