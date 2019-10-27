#F-строки - это литерал строки с буквой f перед ним. Внутри f-строки в паре фигурных скобок указываются имена переменных,
#которые надо подставить:
ip = '10.1.1.1'
mask = 24

print(f"IP: {ip}, mask: {mask}")
#Кроме подстановки значений переменных, в фигурных скобках можно писать выражения:
octets = ['10', '1', '1', '1']
mask = 24
print(f"IP: {'.'.join(octets)}, mask: {mask}")

#После двоеточия в f-строках можно указывать те же значения, что и при использовании format:
oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
print(f'''
IP address:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}''')

#При использовании f-строк в циклах,
# f-строку надо писать в теле цикла, чтобы она «подхватывала» новые значения переменных на каждой итерации:
ip_list = ['10.1.1.1/24', '10.2.2.2/24', '10.3.3.3/24']

for ip_address in ip_list:
    ip, mask = ip_address.split('/')
    print(f"IP: {ip}, mask: {mask}")

#Выравнивание столбцами:
topology = [['sw1', 'Gi0/1', 'r1', 'Gi0/2'],
            ['sw1', 'Gi0/2', 'r2', 'Gi0/1'],
            ['sw1', 'Gi0/3', 'r3', 'Gi0/0'],
            ['sw1', 'Gi0/5', 'sw4', 'Gi0/2']]

for connection in topology:
    l_device, l_port, r_device, r_port = connection
    print(f'{l_device:10} {l_port:7} {r_device:10} {r_port:7}')

#Работа со словарями
session_stats = {'done': 10, 'todo': 5}

if session_stats['done']:
    print(f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}")
else:
    print(f"Good job! All {session_stats['done']} pomodoros done!")