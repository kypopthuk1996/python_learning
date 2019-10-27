# -*- coding: utf-8 -*-
#Сделать копию скрипта задания 7.3.
#Дополнить скрипт: Отсортировать вывод по номеру VLAN.

list_new = []
list1 = []
double_list = []
with open('CAM_table.txt', 'r') as f:
    for list_n in f.read().split('\n'):
        if list_n.count('Gi0') == 1:
            list_new.append(list_n)
list_new = '\n'.join(list_new).split(' ')
for ind in list_new:
    if ind != '' and ind != 'DYNAMIC':
        list1.append(ind)
print(list1)

