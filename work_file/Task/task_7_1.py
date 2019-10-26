# -*- coding: utf-8 -*-
#Аналогично заданию 4.6 обработать строки из файла ospf.txt и вывести информацию по каждой в таком виде:

#Protocol:              OSPF
#Prefix:                10.0.24.0/24
#AD/Metric:             110/41
#Next-Hop:              10.0.13.3
#Last update:           3d18h
#Outbound Interface:    FastEthernet0/0

with open('ospf.txt', 'r') as f:
    line = f.read()
    pr = line.split(' ')
    print("{:15}        {:15}".format('Protokol:', 'OSPF'))
    print("{:15}        {:15}".format('Prefix:', pr[8]))
    print("{:15}        {:15}".format('AD/Metric:', pr[9]))
    print("{:15}        {:15}".format('Next-hop:', pr[11]))
    print("{:15}        {:15}".format('Last update:', pr[12]))
    print("{:15}    {:15}".format('Outbound interface:', pr[13]))
