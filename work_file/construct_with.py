# -*- coding: utf-8 -*-
#Конструкция with называется менеджер контекста.
#В Python существует более удобный способ работы с файлами, чем те, которые использовались до сих пор - конструкция with:
with open('r1.txt', 'r') as f:
    for line in f:
        print(line)
#Кроме того, конструкция with гарантирует закрытие файла автоматически.

#Открытие двух файлов
#Иногда нужно работать одновременно с двумя файлами. Например, надо записать некоторые строки из одного файла, в другой.
#В таком случае, в блоке with можно открывать два файла таким образом:
with open('r1.txt') as src, open('result.txt', 'w+') as dest:
    for line in src:
        if line.startswith('service'):
            dest.write(line)
    dest.seek(0)
    print(dest.read())