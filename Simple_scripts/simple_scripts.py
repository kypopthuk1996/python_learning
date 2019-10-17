# -*- coding: utf-8 -*-
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n'.join(access_template).format(5))
#join - Возвращает строку, собранную из элементов указанного объекта, поддерживающего итерирование.
