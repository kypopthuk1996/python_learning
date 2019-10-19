# -*- coding: utf-8 -*-
#Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
#Затем вывести информацию о сети и маске в таком формате:

#Network:
#10        1         1         0
#00001010  00000001  00000001  00000000

#Mask:
#/24
#255       255       255       0
#11111111  11111111  11111111  00000000
from sys import argv

net = argv[1]
msk = argv[2]
msk = str('/' + msk)
print('\nNetwork:')

net_list = net.split('.')
a0 = int(net_list[0])
a1 = int(net_list[1])
a2 = int(net_list[2])
a3 = int(net_list[3])

print('{:}       {:}       {:}         {:}'.format(net_list[0], net_list[1], net_list[2], net_list[3]))
print('{:08b} {:08b}  {:08b}  {:08b}'.format(a0, a1, a2, a3))
print('\nMask:')
print(msk)
dr = int(msk[1:])*'1'+'0'*(32-int(msk[1:]))
dr1 = int(dr[:8], 2)
dr2 = int(dr[8:16], 2)
dr3 = int(dr[16:24], 2)
dr4 = int(dr[-8:], 2)

dr5 = int(dr[:8])
dr6 = int(dr[8:16])
dr7 = int(dr[16:24])
dr8 = dr[-8:]

print(str(dr5) + '  ' + str(dr6)+ '  ' + str(dr7) + '  ' + str(dr8))
print(str(dr1) + '  ' + str(dr2)+ '  ' + str(dr3) + '  ' + str(dr4))
