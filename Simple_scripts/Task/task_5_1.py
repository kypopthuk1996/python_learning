# -*- coding: utf-8 -*-
#В задании создан словарь, с информацией о разных устройствах.
#Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
#И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).
#Пример выполнения скрипта:
#Введите имя устройства: r1
#{'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

device = input('Введите имя устройства: ')
print(london_co[device])

#task_5_1_a
#Переделать скрипт из задания 5.1 таким образом,
#чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.

device = input('Введите имя устройства: ')
param = input('Введите имя параметра: ')
print(london_co[device][param])

#task_5_1_b
#Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
#отображался список возможных параметров. Список параметров надо получить из словаря, а не прописывать вручную.

device = input('Введите имя устройства: ')
str1 = str(london_co[device].keys())
str1 = str1.replace('[', '').replace('dict_keys', '').replace('(', '').replace(')', '').replace(']', '')
str1 = str1.replace('\'', '')
param = input('Введите имя параметра (' + str1 + '): ')
print(london_co[device][param])

#task_5_1_c
#Переделать скрипт из задания 5.1b таким образом, чтобы, при запросе параметра,
#которого нет в словаре устройства, отображалось сообщение „Такого параметра нет“.

device = input('Введите имя устройства: ')
str1 = str(london_co[device].keys())
str1 = str1.replace('[', '').replace('dict_keys', '').replace('(', '').replace(')', '').replace(']', '')
str1 = str1.replace('\'', '')
param = input('Введите имя параметра (' + str1 + '): ')
print(london_co[device].get(param, 'Такого параметра нет'))

#task_5_1_d
#Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
#пользователь мог вводить название параметра в любом регистре.

device = input('Введите имя устройства: ')
str1 = str(london_co[device].keys())
str1 = str1.replace('[', '').replace('dict_keys', '').replace('(', '').replace(')', '').replace(']', '')
str1 = str1.replace('\'', '')
param = input('Введите имя параметра (' + str1 + '): ')
print(london_co[device].get(param.lower(), 'Такого параметра нет'))
