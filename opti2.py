import random

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def optimize_satellite(file_path):
    # Lecture des données du fichier
    with open(file_path, 'r') as file:
        max_distance = float(file.readline().strip())
        num_points = int(file.readline().strip())
        points = [tuple(map(int, line.strip().split())) for line in file]

    # Choix aléatoire du point de départ
    start_point = random.choice(points)
    current_point = start_point
    solution = [points.index(start_point)]
    visited = {points.index(start_point)}

    # Recherche locale
    while len(visited) < num_points:
        min_distance = float('inf')
        closest_point = None

        for i, point in enumerate(points):
            if i not in visited:
                d = distance(current_point, point)
                if d < min_distance:
                    min_distance = d
                    closest_point = point

        if min_distance <= max_distance:
            current_point = closest_point
            current_index = points.index(current_point)
            solution.append(current_index)
            visited.add(current_index)
        else:
            # Si aucun point non visité n'est atteignable, on choisit un nouveau point de départ
            unvisited_points = [point for i, point in enumerate(points) if i not in visited]
            if unvisited_points:
                start_point = random.choice(unvisited_points)
                current_point = start_point
                solution.append(points.index(start_point))
                visited.add(points.index(start_point))
            else:
                break

    return solution

# Exemple d'utilisation avec le premier jeu de données
file_path = 'data.txt'
solution = optimize_satellite(file_path)
print(solution)
numbers = solution
result = ' '.join(str(num) for num in numbers)
print(result)