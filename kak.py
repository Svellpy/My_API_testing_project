# file_cheatsheet.py

# 📌 Открытие файла для записи (перезаписывает всё содержимое)
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('Программа запущена\n')  # Запись строки в файл

# 📌 Открытие файла для добавления (не стирает старое содержимое)
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Следующий шаг...\n')  # Добавление новой строки

# 📌 Запись нескольких строк
lines = ['Шаг 1 выполнен\n', 'Шаг 2 выполнен\n']
with open('log.txt', 'a', encoding='utf-8') as f:
    f.writelines(lines)

# 📌 Чтение всего содержимого файла
with open('log.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print('Весь файл:\n', content)

# 📌 Чтение построчно (список строк)
with open('log.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print('Построчно:\n', lines)

# 📌 Пример логгирования с текущим временем
from datetime import datetime

def log(message: str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] {message}\n')

log('Процесс завершён успешно')

# 📌 Проверка наличия файла перед чтением
import os

if os.path.exists('log.txt'):
    with open('log.txt', 'r', encoding='utf-8') as f:
        print(f'Содержимое log.txt:\n{f.read()}')
else:
    print('Файл не найден')
