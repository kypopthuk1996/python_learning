# -*- coding: utf-8 -*-

#List - последовательность элементов, разделенных между собой запятой и заключенных в квадратные скобки
list1 = [10, 20, 30, 'dog1']
print(list1)

#Создание списка при помощи команды list
gh=list('Dmitriy')
print(gh)
#Обращение к элементы списка начинается с 0 позиции
print(gh[1])
#Перевернуть список - reverse
list1.reverse()
#Изменение элемента списка
list1[1] = 'Atom'
print(list1)
#Можно создавать список из списков
interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
print(interfaces[0][0])
#Подсчет количества эдементов в списке
print(len(interfaces[0]))
