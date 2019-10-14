# -*- coding: utf-8 -*-

#Форматирование строк

#format - подставляется значение в format на место {}
string="interface FastEth0/{}"
print(string.format("1"))
#print(f"This a {string}")
#Вывод столбцами по 15 символов
vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']
print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))

#Конвертирование сразу в двочиных формат
gg='{:b} {:b} {:b} {:b}'.format(192, 100, 1, 1)
print(gg)

#Дополнить числа нулями, вместо пробелов
hh='{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1)
print(hh)

#Задание имени для подстановки
kk='{ip}/{mask}'.format(mask=24, ip='10.1.1.1')
print(kk)

# Python3 program introducing f-string
val = 'Geeks'
print(f'{val}for{val} is a portal for {val}.')


name = 'Tushar'

age = 23
print(f'Hello, My name is {name} and Im {age} years old.')
