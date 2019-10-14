# -*- coding: utf-8 -*-
# Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX XXXX.XXXX.XXXX
mac = 'AAAA:BBBB:CCCC'
mac = mac + ':'
print(2*mac.replace(':', '.'))
