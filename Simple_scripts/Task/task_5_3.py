# -*- coding: utf-8 -*-
#Скрипт должен запрашивать у пользователя:

#информацию о режиме интерфейса (access/trunk)
#номере интерфейса (тип и номер, вида Gi0/3)
#номер VLANа (для режима trunk будет вводиться список VLANов)
#В зависимости от выбранного режима, на стандартный поток вывода,
#должна возвращаться соответствующая конфигурация access или trunk
#(шаблоны команд находятся в списках access_template и trunk_template).

#При этом, сначала должна идти строка interface и подставлен номер интерфейса,
#а затем соответствующий шаблон, в который подставлен номер VLANа
#(или список VLANов).

#task 5_3
#mode = input('Введите режим работы интерфейса (access/trunk): ')
#interface = input('Введите тип и номер интерфейса: ')
#vlan = input('Введите номер влан(ов): ')

#access_template = [
#    'switchport mode access', 'switchport access vlan {}',
#    'switchport nonegotiate', 'spanning-tree portfast',
#    'spanning-tree bpduguard enable'
#]

#trunk_template = [
#    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
#    'switchport trunk allowed vlan {}'
#]

#print(f'interface {interface}')
#print('\n'.join(access_template).format(vlan))
#new_dict = dict(access = access_template, trunk = trunk_template)
#print('\n'.join(new_dict[mode]).format(vlan))

#task 5_3_a
mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
quest = dict(access = 'Введите номер VLAN: ', trunk = 'Введите разрешенные VLANы: ')
vlan = input(quest[mode])

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

print(f'interface {interface}')
#print('\n'.join(access_template).format(vlan))
new_dict = dict(access = access_template, trunk = trunk_template)
print('\n'.join(new_dict[mode]).format(vlan))
