import math

RADIUS: float = 6371.01


def distance_between_cities(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) +
                                  math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    return distance


distance = distance_between_cities(50.45, 30.523, 51.5072, -0.1275)
print(distance)
