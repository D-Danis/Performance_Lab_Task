# Задание 4
# Дан массив целых чисел nums.
# Напишите программу, выводящую минимальное количество ходов, требуемых для
# приведения всех элементов к одному числу.
# За один ход можно уменьшить или увеличить число массива на 1
# Пример:
# nums = [1, 2, 3]
# Решение: [1, 2, 3] => [2, 2, 3] => [2, 2, 2].
# Минимальное количество ходов: 2
# Элементы массива читаются из файла, переданного в качестве аргумента
# командной строки!
# Пример:
# На вход подаётся файл с содержимым:
# 1
# 10
# 2
# 9
# Вывод в консоль: 16



import sys


def load_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


def median_nums(nums):
    # Находим медиану
    nums = sorted(nums)
    mid = len(nums) // 2
    return int((nums[mid] + nums[~mid]) / 2 if len(nums) % 2 == 0 else nums[mid])


def min_moves_to_equal(nums):
    median = median_nums(nums)
    total_moves = sum(abs(num - median) for num in nums)  # Считаем общие ходы
    return total_moves

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 task_4.py <numbers_file>")
        sys.exit(1)

    numbers = sys.argv[1]
    nums = load_numbers(numbers)
    result = min_moves_to_equal(nums)
    print(result)

if __name__ == "__main__":
    main()


# python3 task_4.py numbers.txt