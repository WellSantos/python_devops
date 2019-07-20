#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    with open("teste.txt",'r') as f:
        #for l in f.readlines(): #imprime o caracter \n(newline)
        for l in f.read().splitlines(): #NÃO imprime o caracter \n(newline)
           print l
except Exception as e:
    print "Erro: %s"%e
