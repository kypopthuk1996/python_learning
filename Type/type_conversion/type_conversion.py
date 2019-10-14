# -*- coding: utf-8 -*-
# Преобразование строки в integer - int()
hg = '10'
print(int(hg))

fe = '101011'
print(int(fe, 2)) # преобразование двоичного числа с десятичное
print(bin(int(hg))) # преобразование десятичного числа в двоичное
print(hex(int(hg))) # преобразование десятичного числа в десятичное
print(list(fe)) # преобразование в список
print(set(fe)) # преобразование во множество
print(tuple(fe)) # преобразование в кортеж

# проверка типа на число - isdigit()
print(hg.isdigit())

# состоит ли строка из одних букв - isalpha()
print(hg.isalpha())

# состоит ли строка из букв и цифр - isalnum()
print(hg.isalnum())

# Проверка типа данных
print(type(hg))
print(type(hg) is str)
