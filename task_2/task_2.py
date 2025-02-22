# Задание 2
# Напишите программу, которая рассчитывает положение точки относительно
# окружности.
# Координаты центра окружности и его радиус считываются из файла 1
# Пример:
# 1 1
# 5
# Координаты точек считываются из файла 2
# Пример:
# 0 0
# 1 6
# 6 6
# Вывод для данных примеров файлов:
# 1
# 0
# 2
# Пути к файлам передаются программе в качестве аргументов!
# ● файл с координатами и радиусом окружности - 1 аргумент;
# ● файл с координатами точек - 2 аргумент;
# ● координаты - рациональные числа в диапазоне от 10-38 до 1038;
# ● количество точек от 1 до 100;
# ● вывод каждого положения точки заканчивается символом новой строки;
# ● соответствия ответов:
# ○ 0 - точка лежит на окружности
# ○ 1 - точка внутри
# ○ 2 - точка снаружи.
# Вывод программы в консоль.

import sys

def read_circle_data(file_path):
    # считывает координаты центра окружности и радиус из файла.
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (center_x, center_y, radius)

def read_points(file_path):
    # считывает координаты точек из файла
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def point_position(circle, point):
    # определяет положение точки относительно окружности, 
    # сравнивая квадрат расстояния от точки до центра окружности с квадратом радиуса.
    center_x, center_y, radius = circle
    point_x, point_y = point
    distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
    radius_squared = radius ** 2
    
    if distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    elif distance_squared == radius_squared:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 task_2.py <circle_file> <dot_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    # чтение данных и вывод результатов для каждой точки.
    circle = read_circle_data(circle_file)
    points = read_points(points_file)

    for point in points:
        position = point_position(circle, point)
        print(position)

# python3 task_2.py circle.txt dot.txt"