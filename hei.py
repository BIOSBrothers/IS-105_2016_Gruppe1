# -*- coding: utf-8 -*-
from sys import argv

def func1(name1, name2):
    return "Hei, " + name1 + "og " + name2

name1, name2 = argv[1], argv[2]
print func1(name1,name2)