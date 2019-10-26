# -*- coding: utf-8 -*-
from sys import argv

#Дополнить скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
# скрипт должен записать полученные строки в файл config_sw1_cleared.txt

#При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
# Строки, которые начинаются на ! отфильтровывать не нужно.
ignore = ['duplex', 'alias', 'Current configuration']

lines_2 = []
lines_3 = []

name_file = argv[1]
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
with open('config2.txt', 'w+') as d:
    d.writelines(lines_3)
    d.seek(0)
    print(d.read())

