# -*- coding: utf-8 -*-
#Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

ip_correct = False

while not ip_correct:
    a = 0
    chk_1 = True
    net = input('Введите IP-адрес: ')
    net_list = net.split('.')
    len_new_list = len(net_list)
    if len_new_list != 4:
        print('Неправильный IP-адрес по длине')
        chk_1 = False
        continue
    elif chk_1 == True:
        for ind_n in net_list:
            a += 1
            if int(ind_n) not in range(0, 256):
                print('Неправильный  IP-адрес по диапозону')
                a -= 1
            if a == 4:
                ip_correct = True

i = 0
j = 0
m = 0
if int(net_list[0]) in range(1, 224):
    print('Unicast')
elif int(net_list[0]) in range(224, 240):
    print('Multicast')
else:
    for id in net_list:
        m += 1
        if id == '255':
            i += 1
            if i == 4:
                print('local broadcast')
        elif id == '0':
            j += 1
            if j == 4:
                print('unassigned')
        else:
            if m == 4:
                print('unused')
