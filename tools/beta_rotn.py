# -*- coding: utf-8 -*-

import sys

def rotn(s,n):
    res = ""
    for i in s:
        od = ord(i)
        
        if 65 <= od <= 90:
            od -= 65
            od += n
            od %= 26
            res += chr(od+65)
        elif 97 <= od <= 97+25:
            od -= 97
            od += n
            od %= 26
            res += chr(od+97)
        else:
            res += i
    return res

args = sys.argv
if len(args) != 3:
    print("lrotn [sentence] [n]")
    exit(1)
s, n = args[1:]
try:
    n = int(n)
except ValueError:
    print(n,"is not integer")
    exit(1)

print(rotn(s, n))
exit(0)