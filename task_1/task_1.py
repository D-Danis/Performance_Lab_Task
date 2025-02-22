# Задание 1
# Круговой массив - массив из элементов, в котором по достижению конца массива
# следующим элементом будет снова первый. Массив задается числом n, то есть
# представляет собой числа от 1 до n.
# Пример кругового массива для n=3:
# Напишите программу, которая выводит путь, по которому, двигаясь интервалом длины
# m по заданному массиву, концом будет являться первый элемент.
# Началом одного интервала является конец предыдущего.
# Путь - массив из начальных элементов полученных интервалов.
# Пример 1
# n = 4, m = 3
# Решение:
# Круговой массив: 1234
# При длине обхода 3 получаем интервалы: 123, 341 Полученный путь: 13
# Пример 2
# n = 5, m = 4
# Решение:
# Круговой массив: 12345
# При длине обхода 4 получаем интервалы: 1234, 4512, 2345, 5123, 3451
# Полученный путь: 14253
# Параметры передаются в качестве аргументов командной строки!
# Например, для последнего примера на вход подаются аргументы: 5 4, ожидаемый
# вывод в консоль: 14253

import sys

def circular_array_path(n, m):
    # Создаем круговой массив
    circular_array = list(range(1, n + 1))
    
    # Начальная позиция
    start_index = 0
    path = []
    j=0
    # Пока не вернемся к первому элементу
    while True:
        # Получаем текущий интервал
        interval = [circular_array[(start_index + i + j) % n] for i in range(m)]
        # Добавляем первый элемент интервала в путь
        path.append(interval[0])
        
        j+=m
        
        # Обновляем начальный индекс
        start_index = (start_index + m) % n

        # Если вернулись к началу, выходим из цикла
        if start_index == 0:
            break
    
    return ''.join(map(str, path))

if __name__ == "__main__":
    # Получаем аргументы из командной строки
    if len(sys.argv) != 3:
        print("Usage: python3 task_1.py <n> <m>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    # Вызываем функцию и выводим результат
    result = circular_array_path(n, m)
    print(result)
    
# python3 task_1.py 5 4