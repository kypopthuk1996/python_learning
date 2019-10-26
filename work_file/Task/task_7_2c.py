# -*- coding: utf-8 -*-
from sys import argv
#Переделать скрипт из задания 7.2b: передавать как аргументы скрипту:
#имя исходного файла конфигурации
#имя итогового файла конфигурации
#Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
#в которых содержатся слова из списка ignore. И записать остальные строки в итоговый файл.
ignore = ['duplex', 'alias', 'Current configuration']

lines_2 = []
lines_3 = []

name_file = argv[1]
new_file = argv[2]

with open(name_file, 'r') as f:
    for line in f.read().split('\n'):
        lines_2.append(line)

m = 0
for val in lines_2:
    m = 0
    for ind in ignore:
        if val.count(ind) == 0:
            m += 1
        if m == 3:
            lines_3.append(val)

lines_3 = '\n'.join(lines_3)
with open(new_file, 'w+') as d:
    d.writelines(lines_3)
    d.seek(0)
    print(d.read())

