# Импортируйте необходимые модули:

   import csv
   import json

# Определите функцию task():

   def task() -> None:
       input_filename = "input.csv"
       output_filename = "input.json"

       # Считываем содержимое CSV файла
       with open(input_filename, mode='r', newline='', encoding='utf-8') as csvfile:
           reader = csv.DictReader(csvfile)

           # Сохраняем строки в список
           data = [row for row in reader]

       # Записываем данные в формате JSON с отступами 4
       with open(output_filename, mode='w', encoding='utf-8') as jsonfile:
           json.dump(data, jsonfile, indent=4)

# Вызовите функцию в блоке if __name__ == '__main__':, чтобы проверить работу:

   if __name__ == '__main__':
       task()
       with open("input.json") as output_f:
           for line in output_f:
               print(line, end="")