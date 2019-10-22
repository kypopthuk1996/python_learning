# -*- coding: utf-8 -*-
#Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
#Определить тип IP-адреса.
#В зависимости от типа адреса, вывести на стандартный поток вывода:
#„unicast“ - если первый байт в диапазоне 1-223
#„multicast“ - если первый байт в диапазоне 224-239
#„local broadcast“ - если IP-адрес равен 255.255.255.255
#„unassigned“ - если IP-адрес равен 0.0.0.0
#„unused“ - во всех остальных случаях
net = input('Введите IP-адрес: ')
net_list = net.split('.')
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
