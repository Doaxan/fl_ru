"""
Решение для fl.ru
"Нужно перенести на python 25-строчный скрипт, который принимает на вход csv файл, обфусцирует случайным образом его содержимое."
https://www.fl.ru/projects/4183419/portirovat-25-strochnyiy-perl-skript-v-python.html#hiddenOfferInfo

re не использовалось в целях достижения большей производительности
"""
import csv
import string
from random import random


def get_element(element):
    new_element = ''
    for symbol in element:
        if symbol.isdigit():
            new_element += string.digits[int(random() * (len(string.digits) - 1))]
        elif symbol.isalpha():
            new_symbol = string.ascii_lowercase[int(random() * (len(string.ascii_lowercase) - 1))]
            if symbol.isupper(): new_symbol = new_symbol.upper()
            new_element += new_symbol
        else:
            new_element += symbol
    return new_element


def main():
    result = []
    while True:
        value = input()
        reader = csv.reader(value.splitlines(), delimiter='\t')
        data = list(reader)
        if data and len(result) < len(data[0]):
            result.extend([{} for i in range(len(data[0]) - len(result))])
        new_csv = []
        for row in data:
            new_row = []
            for i, elem in enumerate(row):
                if elem not in result[i]:
                    result[i][elem] = get_element(elem)
                new_row.append(result[i][elem])
            new_csv.append(new_row)
        for row in new_csv:
            print('\t'.join(row))


if __name__ == '__main__':
    main()
