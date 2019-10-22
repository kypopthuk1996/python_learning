# -*- coding: utf-8 -*-
#Добавить проверку введенного IP-адреса.
#Адрес считается корректно заданным, если он:
#состоит из 4 чисел разделенных точкой,
#каждое число в диапазоне от 0 до 255.
#Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“
net = input('Введите IP-адрес: ')
net_list = net.split('.')
len_new_list = len(net_list)
if len_new_list != 4:
    print('Неправильный IP-адрес')
else:
    for ind_n in net_list:
        if int(ind_n) not in range(0, 256):
            print('Неправильный  IP-адрес')
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
