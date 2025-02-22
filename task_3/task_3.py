# Задание 3
# На вход в качестве аргументов программы поступают три пути к файлу (в приложении
# к заданию находятся примеры этих файлов):
# ● values.json содержит результаты прохождения тестов с уникальными id
# ● tests.json содержит структуру для построения отчета на основе прошедших
# тестов (вложенность может быть большей, чем в примере)
# ● report.json - сюда записывается результат.
# Напишите программу, которая формирует файл report.json с заполненными полями
# value для структуры tests.json на основании values.json.
# Структура report.json такая же, как у tests.json, только заполнены поля “value”.
# На вход программы передается три пути к файлу!

import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def fill_report_structure(tests, values):
  
    if isinstance(tests, dict):
        # print(values)
        # Если текущий уровень - словарь, проверяем поля
        if 'id' in tests.keys():
            for item in values['values']:
                if tests['id'] == item['id']:
                    tests['value'] = item['value']
        
        for key, value in tests.items():
            if isinstance(value, (dict, list)):
                fill_report_structure(value, values)
                
    elif isinstance(tests, list):
        # Если текущий уровень - список, проходим по элементам
        for item in tests:
            fill_report_structure(item, values)


def main(values_file, tests_file, report_file):
    values = load_json(values_file)
    tests = load_json(tests_file)

    fill_report_structure(tests, values)

    with open(report_file, 'w') as file:
        json.dump(tests, file, indent=4)





if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 task_3.py <values_file> <tests_file> <report_file>")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)

# python3 task_3.py values.json tests.json report.json