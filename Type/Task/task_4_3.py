# -*- coding: utf-8 -*-
# Получить из строки config список VLANов вида: ['1', '3', '10', '20', '30', '100']

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(config.split( ))
config = config.split( )
config = config[-1].split(',')
print(config)
