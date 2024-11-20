# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding='utf-8') as csvf:  # TODO считать содержимое csv файла
        data = [row for row in csv.DictReader(csvf)]
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(data, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)  # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

