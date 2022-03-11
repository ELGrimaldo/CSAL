import math
from typing import List

coordinates = [ (-2, 5), (-4, 1), (-1, 1), 
                (1, 3), (2, 2), (4,1), 
                (-3, 3), (-2,-3), (-1, 5 ), 
                (2, -1), (1, -3), (4, -1)]

def closestTwoPoints(coord : List) -> str:
    minimum_distance = float('inf')

    for point_a in range(0, len(coordinates)):  
        for point_b in range(0, len(coordinates)):
            if point_a == point_b:
                pass
            else:
                distance = math.sqrt(((coord[point_a][0] - coord[point_b][0])**2) + ((coord[point_a][1] - coord[point_b][1])**2))
                
                if distance < minimum_distance:
                    minimum_distance = distance
                
    print(minimum_distance)
closestTwoPoints(coordinates)
print(1<<4)