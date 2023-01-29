#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

pwd = os.getcwd()
if not os.path.isfile(pwd+"/.raw_uekirc"):
    print("raw_uekirc not found.")
    exit(1)

with open(pwd+"/.raw_uekirc", "r") as f:
    aliases = f.readlines()

with open(pwd+"/uekirc", "w") as f:
    f.write("")

f = open(pwd+"/uekirc", "a")
for alias in aliases:
    alias_name, filename = alias.split()
    fullalias = "alias " + alias_name + "=\"python3 " + pwd + "/tools/" + filename + "\"\n"
    f.write(fullalias)

print("Complete! please run this command")
print("echo \"source",pwd+"/uekirc\"",">> [your rcfile]; source [your rcfile]")

exit(0)