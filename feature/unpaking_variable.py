#Распаковка переменных - это специальный синтаксис, который позволяет присваивать переменным элементы итерируемого объекта.
interface = ['FastEthernet0/1', '10.1.1.1', 'up', 'up']
intf, ip, status, protocol = interface
print(ip)

#Замена ненужных элементов _
#Часто из всех элементов итерируемого объекта нужны только некоторые.
#При этом синтаксис распаковки требует указать ровно столько переменных, сколько элементов в итерируемом объекте.
#Если, например, из строки line надо получить только VLAN, MAC и интерфейс, надо все равно указать переменную для типа записи:
dhcp = '00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1'
mac, ip, _, _, vlan, intf = dhcp.split()
print(vlan)

#Распаковка переменных поддерживает специальный синтаксис, который позволяет распаковывать несколько элементов в один.
# Если поставить * перед именем переменной, в нее запишутся все элементы, кроме тех, что присвоены явно.
#Например, так можно получить первый элемент в переменную first, а остальные в rest:
vlans = [10, 11, 13, 30]
first, *rest = vlans
print(rest)

#Таким образом можно указать, что нужен первый, второй и последний элемент:
cdp = 'SW1     Eth 0/0    140   S I   WS-C3750-  Eth 0/1'
name, l_intf, *other, r_intf = cdp.split()
print(r_intf)
#Эти примеры показывают, что распаковывать можно не только списки, кортежи и строки, но и любой другой итерируемый объект.
first, *rest = range(1,6)
print(rest)

#Пример цикла, который проходится по ключам:
access_template = ['switchport mode access',
                    'switchport access vlan',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']
    

access = {'0/12':10,
            '0/14':11,
            '0/16':17}
    
for intf, vlan in access.items():
         print('interface FastEthernet' + intf)
         for command in access_template:
             if command.endswith('access vlan'):
                 print(' {} {}'.format(command, vlan))
             else:
                 print(' {}'.format(command))
