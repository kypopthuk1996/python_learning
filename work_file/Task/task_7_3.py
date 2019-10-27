# -*- coding: utf-8 -*-
#Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка, где есть MAC-адрес,
#должна быть обработана таким образом, чтобы на стандартный поток вывода была выведена
# таблица вида (показаны не все строки из файла):

#100    01bb.c580.7000   Gi0/1
#200    0a4b.c380.7000   Gi0/2
#300    a2ab.c5a0.7000   Gi0/3
#100    0a1b.1c80.7000   Gi0/4
#500    02b1.3c80.7000   Gi0/5
#200    1a4b.c580.7000   Gi0/6
#300    0a1b.5c80.7000   Gi0/7

list_new = []
with open('CAM_table.txt', 'r') as f:
    for list in f.read().split('\n'):
        if list.count('Gi0') == 1:
            list_new.append(list)
list_new = '\n'.join(list_new)
print(list_new.replace('DYNAMIC', '').replace('   ', ' '))