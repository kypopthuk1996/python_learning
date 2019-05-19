#Строка
print('Hello')

#Сложение строк
a='Hello'
b='World'
print(a+' '+b)

#Умножение строк
print(a*5)


#Обращение к конкретному символу
print(a[1]) #Обращение к конкретному символу (начиная с 0)
print(a[-1]) #Для обращения с конца следует начинать с -1

#Срезы строк
print(a[1:4]) #Срез строк (не включает последнее число)
print(a[2:]) #Срез до конца строки (не включает 1 число)
print(a[-2:]) #Срез последних 2 символов

#Cрез с шагом
c1='0123456789'
print(c1[1::2]) #Все нечетные цифры
print(c1[0::2]) #Все четные цифры
print(c1[::-1]) #Срез в обратном порядке

#Методы для строк
#upper - перевод в заглавные буквы
string="FastEthernet"
print(string.upper())

#lower - перевод в строчные буквы
print(string.lower())

#swapcase - смена заглавных на строчные
print(string.swapcase())

#count - подсчет того, сколько раз символ или подстрока встречаются в строке
hq="alo, alo, Alo, al"
print(hq.count("alo"))

#find - поиск до символа, выводит позицию 1 совпадения
print(string.find("Et"))

#startswitch - начинается ли строка на эти символы
print(string.startswith("Fas"))

#endswitch - заканчивается ли строка на эти смволы
print(string.endswith("e"))

#replace - замена символов в строке на другие
print(string.replace('Fast', 'Gigabit'))

#strip - удаляет в конце и в начале спец символы, можно передать свои
gg='[12.42]'
print(gg)
print(gg.strip('[]'))

#split - разбивает строку на части, используя разделитель
string1 = ' switchport trunk allowed vlan 10,20,30,100-200\n'
com=string1.strip().split()
print(com)
print(com[-1].split(','))




