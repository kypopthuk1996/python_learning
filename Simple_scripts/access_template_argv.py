# -*- coding: utf-8 -*-
from sys import argv

#Передача аргументов скрипту
interface = argv[1]
vlan = argv[2]

#argv - это список
#все аргументы находятся в списке в виде строк
#argv содержит не только аргументы, которые передали скрипту, но и название самого скрипта

#В данном случае в списке argv находятся такие элементы:
#['access_template_argv.py', 'Gi0/7', '4']

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

# python3.7 access_template_argv.py 12 8
