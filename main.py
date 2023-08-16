# #Решение номер 1
# string = input('Введите слова:\n ')
# string1 = string.split(',')
# string2 = []
# print(f'Из предложения: {string} - слова удалены')
# for index in string1:
#     if string1.count(index) == 1:
#         string2.append(index)
# print(f"ответ: {', '.join(string2)}")

# Решение номер 2

import os

somelists = []

while True:
    print('1 - Для записи в файл ')
    print('2 - Для чтения из файла')
    print('3 - Для выхода из программы ')

    number = input('Выберите действие из списка: ')

    if number == '1':
        open('text.txt', 'w', encoding='utf-8') # запись в файл
        newline = input('Введите слова через запятую: ')
        with open('text.txt', 'a', encoding='utf-8') as file:
            file.write(newline + '\n')
    elif number == '2':
        with open('text.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    elif number == '3':
        break

print('Программа завершена')


