#Разбор вывода столбцами
#В этом примере будет разбираться вывод команды sh ip int br.
# Из вывода команды нам надо получить соответствия имя интерфейса - IP-адрес.
# То есть имя интерфейса - это ключ словаря, а IP-адрес - значение.
# При этом, соответствие надо делать только для тех интерфейсов, у которых назначен IP-адрес.

result = {}

with open('sh_ip_int_br.txt') as f:
    for line in f:
        line = line.split()
        print(line)

        if line[1][0].isdigit():
            interface, address, *other = line
            result[interface] = address

print(result)

#Получение ключа и значения из разных строк вывода
#Очень часто вывод команд выглядит таким образом, что ключ и значение находятся в разных строках.
# И надо придумать каким образом обрабатывать вывод, чтобы получить нужное соответствие.
#Например, из вывода команды sh ip interface надо получить соответствие имя интерфейса - MTU (файл sh_ip_interface.txt):
#Имя интерфейса находится в строке вида Ethernet0/0 is up, line protocol is up, а MTU в строке вида MTU is 1500 bytes.
#Например, попробуем запоминать каждый раз интерфейс и выводить его значение, когда встречается MTU, вместе со значением MTU:
result = {}

with open('sh_ip_interface.txt') as f:
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
        elif 'MTU is' in line:
            mtu = line.split()[-2]
            result[interface] = mtu

print(result)

#Вложенный словарь
#Если из вывода команды надо получить несколько параметров, очень удобно использовать словарь с вложенным словарем.
#Например, из вывода `sh ip interface` надо получить два параметра: IP-адрес и MTU. Для начала, вывод информации:
result = {}

with open('sh_ip_interface.txt') as f:
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
            result[interface] = {}
        elif 'Internet address' in line:
            ip_address = line.split()[-1]
            result[interface]['ip'] = ip_address
        elif 'MTU' in line:
            mtu = line.split()[-2]
            result[interface]['mtu'] = mtu

print(result)

#Вывод с пустыми значениями
#Иногда, в выводе будут попадаться секции с пустыми значениями.
#Например, в случае с выводом `sh ip interface`, могут попадаться интерфейсы, которые выглядят так:
result = {}

with open('sh_ip_interface.txt') as f:
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
        elif 'Internet address' in line:
            ip_address = line.split()[-1]
            result[interface] = {}
            result[interface]['ip'] = ip_address
        elif 'MTU' in line:
            mtu = line.split()[-2]
            result[interface]['mtu'] = mtu

print(result)