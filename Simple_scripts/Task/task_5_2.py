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

pr_1 = input('Введить ip и маску: ')
print('\nNetwork:')
srh = int(pr_1.find('/'))
net = pr_1[:srh]
msk = pr_1[srh:]
#print(net)
#print(msk)
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
print(dr)
dr1 = int(dr[:8])
dr2 = int(dr[8:16])
dr3 = int(dr[16:24])
dr4 = dr[-8:]

print(int(dr[:8], 2) + '  ' + int(dr[8:16], 2))
#print('{} {} {} {}'.format(dr1, dr2, dr3, dr4))
