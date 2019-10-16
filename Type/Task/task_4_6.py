#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

#Protocol:               OSPF
#Prefix:                 10.0.24.0/24
#AD/Metric:              110/41
#Next-Hop:               10.0.13.3
#Last update:            3d18h
#Outbound Interface:     FastEthernet0/0

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
protokol, p1, prefix, metric, hop, upd, int = ['Protokol:', 'OSPF', 'Prefix:', 'AD/Metrci:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
pr = ospf_route.split(' ')
print("{:15}        {:15}".format(protokol, p1))
print("{:15}        {:15}".format(prefix, pr[8]))
print("{:15}        {:15}".format(metric, pr[9]))
print("{:15}        {:15}".format(hop, pr[11]))
print("{:15}        {:15}".format(upd, pr[12]))
print("{:15}    {:15}".format(int, pr[13]))
