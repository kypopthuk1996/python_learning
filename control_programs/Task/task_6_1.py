# -*- coding: utf-8 -*-
#Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
#Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
new_mac=[]
for num in mac:
    new_mac.append(num.replace(':', '.'))
print(new_mac)
