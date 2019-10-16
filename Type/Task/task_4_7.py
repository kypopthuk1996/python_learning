#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Преобразовать MAC-адрес mac в двоичную строку такого вида:
#101010101010101010111011101110111100110011001100

mac = 'AAAA:BBBB:CCCC'
mac_list = mac.lower().split(':')
#print(mac_list)
#print(int(mac_list[0], 16))
a = int(mac_list[0], 16)
b = int(mac_list[1], 16)
c = int(mac_list[2], 16)
#print(int(mac_list[0], 16), int(mac_list[1], 16), int(mac_list[2], 16))
print('{:b}{:b}{:b}'.format(a,b,c))
