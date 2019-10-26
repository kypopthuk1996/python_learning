# -*- coding: utf-8 -*-
from sys import argv

#Сделать копию скрипта задания 7.2.
#Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
ignore = ['duplex', 'alias', 'Current configuration']

lines_2 = []
lines_3 = []

name_file = argv[1]
with open(name_file, 'r') as f:
    for line in f.read().split('\n'):
        if line != '!':
            lines_2.append(line)
m = 0
for val in lines_2:
    m = 0
    for ind in ignore:
        if val.count(ind) == 0:
            m += 1
        if m == 3:
            lines_3.append(val)

print('-----------------')
for val in lines_3:
    print(val)
