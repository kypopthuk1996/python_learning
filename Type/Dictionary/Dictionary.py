# -*- coding: utf-8 -*-
#Словарь - данные в словаре имеют пары ключ:значение
london = {'name':'Dmitriy', 'location':'Novosibirsk', 'age':23}
print(london['age'])
#Добавление новой пары в словарь
london['work'] = 'Eltex'
print(london['work'])
#В словаре можно использовать в качестве значения словарь
london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }
}
print(london_co['r2']['vendor'])
