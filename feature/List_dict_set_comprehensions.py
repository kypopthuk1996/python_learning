#Python поддерживает специальные выражения, которые позволяют компактно создавать списки, словари и множества.
#На английском эти выражения называются, соответственно:

#List comprehensions
#Dict comprehensions
#Set comprehensions

#Генератор списка - это выражение вида:
vlans = ['vlan {}'.format(num) for num in range(10,16)]
print(vlans)

#В list comprehensions можно использовать выражение if. Таким образом можно добавлять в список только некоторые объекты.
items = ['10', '20', 'a', '30', 'b', '40']
only_digits = [int(item) for item in items if item.isdigit()]
print(only_digits)
#С помощью генератора списка также удобно получать элементы из вложенных словарей:
london_co = {
         'r1' : {
         'hostname': 'london_r1',
         'location': '21 New Globe Walk',
         'vendor': 'Cisco',
         'model': '4451',
         'IOS': '15.4',
         'IP': '10.255.0.1'
         },
         'r2' : {
         'hostname': 'london_r2',
         'location': '21 New Globe Walk',
         'vendor': 'Cisco',
         'model': '4451',
         'IOS': '15.4',
         'IP': '10.255.0.2'
         },
         'sw1' : {
         'hostname': 'london_sw1',
         'location': '21 New Globe Walk',
         'vendor': 'Cisco',
         'model': '3850',
         'IOS': '3.6.XE',
         'IP': '10.255.0.101'
         }
     }

print([london_co[device]['IOS'] for device in london_co])

#Например, в списке vlans находятся несколько вложенных списков с VLAN’ами:
vlans = [[10,21,35], [101, 115, 150], [111, 40, 50]]
result = [vlan for vlan_list in vlans for vlan in vlan_list]
print(result)

#Можно одновременно проходиться по двум последовательностям, используя zip:
vlans = [100, 110, 150, 200]
names = ['mngmt', 'voice', 'video', 'dmz']
result = ['vlan {}\n name {}'.format(vlan, name) for vlan, name in zip(vlans, names)]
print('\n'.join(result))

#Генераторы словарей аналогичны генераторам списков, но они используются для создания словарей.
d = {num: num**2 for num in range(1,11)}
print(d)

#Еще один пример, в котором надо преобразовать существующий словарь и перевести все ключи в нижний регистр
r1 = {'IOS': '15.4',
       'IP': '10.255.0.1',
       'hostname': 'london_r1',
       'location': '21 New Globe Walk',
       'model': '4451',
       'vendor': 'Cisco'}

lower_r1 = {str.lower(key): value for key, value in r1.items()}
print(lower_r1)

#Как и list comprehensions, dict comprehensions можно делать вложенными.
#Попробуем аналогичным образом преобразовать ключи во вложенных словарях:
london_co = {
         'r1' : {
         'hostname': 'london_r1',
         'location': '21 New Globe Walk',
         'vendor': 'Cisco',
         'model': '4451',
         'IOS': '15.4',
         'IP': '10.255.0.1'
         },
         'r2' : {
         'hostname': 'london_r2',
         'location': '21 New Globe Walk',
         'vendor': 'Cisco',
         'model': '4451',
         'IOS': '15.4',
         'IP': '10.255.0.2'
         },
         'sw1' : {
         'hostname': 'london_sw1',
         'location': '21 New Globe Walk',
         'vendor': 'Cisco',
         'model': '3850',
         'IOS': '3.6.XE',
         'IP': '10.255.0.101'
         }
     }
result = {device: {str.lower(key):value for key, value in params.items()} for device, params in london_co.items()}
print(result)

#Set comprehensions (генераторы множеств)
#Генераторы множеств в целом аналогичны генераторам списков.
#Например, надо получить множество с уникальными номерами VLAN’ов:
vlans = [10, '30', 30, 10, '56']
unique_vlans = {int(vlan) for vlan in vlans}
print(unique_vlans)