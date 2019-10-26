# -*- coding: utf-8 -*-
#При записи, очень важно определиться с режимом открытия файла, чтобы случайно его не удалить:

#w - открыть файл для записи. Если файл существует, то его содержимое удаляется
#a - открыть файл для дополнения записи. Данные добавляются в конец файла
#При этом оба режима создают файл, если он не существует.

#Для записи в файл используются такие методы:

#write() - записать в файл одну строку
#writelines() - позволяет передавать в качестве аргумента список строк

#write() - ожидает строку, для записи.
#Для примера, возьмем список строк с конфигурацией:

cfg_lines = ['!',
   'service timestamps debug datetime msec localtime show-timezone year',
     'service timestamps log datetime msec localtime show-timezone year',
     'service password-encryption',
     'service sequence-numbers',
     '!',
     'no ip domain lookup',
     '!',
     'ip ssh version 2',
     '!']

#Открытие файла r2.txt в режиме для записи:
f = open('r2.txt', 'w+')
#Преобразуем список команд в одну большую строку с помощью join:
cfg_lines_as_string = '\n'.join(cfg_lines)
#Запись строки в файл:
f.write(cfg_lines_as_string)
#Аналогично можно добавить строку вручную:
f.write('\nhostname r2')
f.seek(0)
print(f.read())
#После завершения работы с файлом, его необходимо закрыть:
f.close()

#writelines() - ожидает список строк, как аргумент.
g = open('r2.txt', 'w+')
g.writelines(cfg_lines)
g.seek(0)
print(g.read())

#В результате все строки из списка записались в одну строку файла, так как в конце строк не было символа \n.
#Добавить перевод строки можно по-разному. Например, можно просто обработать список в цикле:
cfg_lines_2 = []
for line in cfg_lines:
  cfg_lines_2.append(line + '\n')
print(cfg_lines_2)

#Если итоговый список записать заново в файл, то в нём уже будут переводы строк:
g.writelines(cfg_lines_2)
g.seek(0)
print(g.read())
g.close()
