# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME) as csvf:
        csvReader = csv.DictReader(csvf)  # TODO считать содержимое csv файла
        for row in csvReader:
            data.append(dict(row))
    with open(OUTPUT_FILENAME, 'w') as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)  # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
