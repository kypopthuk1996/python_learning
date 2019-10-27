# -*- coding: utf-8 -*-
from sys import argv

#Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
#имя файла передается как аргумент скрипту.
#Скрипт должен возвращать на стандартный поток вывода команды из переданного конфигурационного файла,
# исключая строки, которые начинаются с !.
#Между строками не должно быть дополнительного символа перевода строки.
lines_2 = []

name_file = argv[1]
with open(name_file, 'r') as f:
    for line in f.read().split('\n'):
        if line != '!':
            lines_2.append(line)
for val in lines_2:
    print(val)