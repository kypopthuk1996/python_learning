# -*- coding: utf-8 -*-
#Кортеж - список, который нельзя изменять. Имеет только права на чтение.
tuple1 = tuple('password',) #простой кортеж
print(tuple1[0])

list1=['i', 'am', 'love', 23] #Кортеж из списка
tr = tuple(list1)
print(tr)

list1[1] = 'love'
print(list1)
