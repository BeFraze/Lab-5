import re
import csv

print('Задание №1')

with open('task1-en.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    words = re.findall(r"\b\w+\.", text)
    fraction = re.findall(r"\b\d+\.\d+\b", text)

    print("Слова, за которыми следует точка:", *words)
    print("Дробные числа:", *fraction)

print('\nЗадание №2')

with open('task2.html', 'r', encoding='utf-8') as file:
    text = file.read()

    pixels = re.findall(r"\b\d+px\b", text)

    print("Значения в пикселях:", *pixels)

print('\nЗадание №3')

with open('task3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    surnames = re.findall(r'[A-Z][a-z]+', text)
    emails = re.findall(r'\w+@\w+.\w+', text)
    dates = re.findall(r'\d{4}-\d\d-\d\d', text)
    urls = re.findall(r'https?://[\w.-]+/', text)

with open('output.csv', 'w', newline='', encoding='utf-8') as output:
    output.write(f'ID, Фамилия, Электронная почта, Дата регистрации, Сайт\n')

    for i in range(len(surnames)):
        output.write(f'{i + 1}, {surnames[i]}, {emails[i]}, {dates[i]}, {urls[i]}\n')
print("Данные успешно обработаны и сохранены в файл: 'output.csv'")

print('\nДоп задание')

with open('task_add.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    dates = re.findall(r'\b(\d{2,4}[-/.]+\d{2,4}[-/.]+\d{2,4})', text)
    emails = re.findall(r'\s(\w+@\w+\.[a-zA-Z]{2,})', text)
    urls = re.findall(r'\b(https?://[\w.-]+)', text)

    print("Даты:", *dates)
    print("Почты:", *emails)
    print("Сайты:", *urls)
