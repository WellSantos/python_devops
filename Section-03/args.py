#!/usr/bin/env python
# -*- coding: utf-8 -*-

servidor = "192.168.0.1"

def calcular(*args):
    if len(args) == 1:
        print "A área do quadrado é",(args[0]*args[0])
    elif len(args) == 2:
        print "A área do retangulo é",(args[0]*args[1])
    elif len(args) == 3:
        print "A área do paralelepipedo é",(args[0]*args[1]*args[2])

calcular(3)
calcular(3,5)
calcular(3,5,7)
