# -*- coding: utf-8 -*-
#В Python есть несколько методов чтения файла:

#read() - считывает содержимое файла в строку
#readline() - считывает файл построчно
#readlines() - считывает строки файла и создает список из строк
#read()
#Метод read() - считывает весь файл в одну строку.
#Пример использования метода read():
f = open('r1.txt')
print(f.read())
print(f.read())
#При повторном чтении файла в 3 строке, отображается пустая строка.
# Так происходит из-за того, что при вызове метода read(), считывается весь файл.
# И после того, как файл был считан, курсор остается в конце файла.
# Управлять положением курсора можно с помощью метода seek().

#Построчно файл можно считать с помощью метода readline():
d = open('r1.txt')
print(d.readline())
print(d.readline())

#Но чаще всего проще пройтись по объекту file в цикле, не используя методы read...:
k = open('r1.txt')
for line in k:
    print(line)
#Еще один полезный метод - readlines(). Он считывает строки файла в список:

g = open('r1.txt')
print(g.readlines())

#Если нужно получить строки файла, но без перевода строки в конце,
#можно воспользоваться методом split и как разделитель, указать символ \n:
y = open('r1.txt')
print(y.read().split('\n'))

#Обратите внимание, что последний элемент списка - пустая строка.
#Если перед выполнением split(), воспользоваться методом rstrip(), список будет без пустой строки в конце:

a = open('r1.txt')
print(a.read().rstrip().split('\n'))

#seek() - До сих пор, файл каждый раз приходилось открывать заново, чтобы снова его считать.
# Так происходит из-за того, что после методов чтения, курсор находится в конце файла.
# И повторное чтение возвращает пустую строку.
#Чтобы ещё раз считать информацию из файла, нужно воспользоваться методом seek,
# который перемещает курсор в необходимое положение.
#с помощью метода seek можно перейти в начало файла (0 означает начало файла):
e = open('r1.txt')
print(e.read())
e.seek(0)
print(e.read())