# -*- coding: utf-8 -*-
#Цикл for перебирает по одному элементы указанной последовательности и выполняет действия,
#которые указаны в блоке for, для каждого элемента.

#Примеры последовательностей элементов, по которым может проходиться цикл for:

#строка
#список
#словарь
#Функция range
#любой Итерируемый объект

words = ['list', 'dict', 'tuple']
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(upper_words)

#Иногда в цикле необходимо использовать последовательность чисел.
#В этом случае, лучше всего использовать функцию Функция range
for i in range(10):
    print('interface FastEthernet0/{}'.format(i))

#Когда цикл идет по словарю, то фактически он проходится по ключам:
r1 = {
'ios': '15.4',
'ip': '10.255.0.1',
'hostname': 'london_r1',
'location': '21 New Globe Walk',
'model': '4451',
'vendor': 'Cisco'}
for k in r1:
    print(k)

#Проход по ключам и значению в словаре
for key, value in r1.items():
    print(key + ' => ' + value)
