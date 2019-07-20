#!/usr/bin/env python
# -*- coding: utf-8 -*-

def descobreDicionario(**kwargs):
    for k in kwargs.keys():
        print "A chave: %s" %k
        print "tem o valor de: %s"%kwargs[k]

descobreDicionario(nome="Well Santos")
descobreDicionario(figura="Jimi Hendrix")
