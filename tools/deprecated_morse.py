# -*- coding: utf-8 -*-

import sys

def morse(s,dt,ds,p):
    res = ""
    err = ""
    err_list = []
    non = {}
    decome_map = {"._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E", ".._.": "F", "__.": "G", "....": "H", "..": "I", ".___": "J", "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O", ".__.": "P", "__._": "Q", "._.": "R", "...": "S", "_": "T", ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y", "__..": "Z",
                  '.____': '1', '..___': '2', '...__': '3', '...._': '4', '.....': '5', '_....': '6', '__...': '7', '___..': '8', '____.': '9', '_____': '0'}
    tmp_s = set(s)
    if len(tmp_s) > 3:
        print("Too many elements")
        exit(1)
    if dt == ds or dt == p or ds == p:
        print("Duplicate the arguments")
        exit(1)
    f = False
    for i in tmp_s:
        if not i in [dt, ds, p]:
            err_list.append("\""+i+"\"")
            f = True
    if f:
        print(*err_list,sep=", ",end=" is not included in the arguments\n")
        exit(1)
    a = s.split(p)
    if "" in a:
        print("Warning!: NULL in morse")
    for i in a:
        save_i = i
        if ds == ".":
            i = i.replace(dt, "0")
            i = i.replace(ds, "_")
            i = i.replace("0", ".")
        else:
            i = i.replace(dt, ".")
            i = i.replace(ds, "_")
        if i in decome_map:
            res += decome_map[i]
            err += " "
        else:
            res += " "
            err += "^"
            non.setdefault(save_i+"("+i+")", 0)
            non[save_i+"("+i+")"] += 1
    if non:
        print(res)
        print(err)
        print("Unknown\tQuantity")
        for i in non:
            print(i+"\t"+str(non[i]))
    else:
        print(res)
    return



args = sys.argv
if len(args) != 5:
    print("lmorse [sentence] [dot] [dash] [separation]")
    exit(1)
s, dt, ds, p = args[1:]
if len(dt) + len(ds) + len(p) != 3:
    print("Sorry, use one character for the argument")
    print("lmorse is beta version...")
    exit(1)

morse(s, dt, ds, p)
exit(0)