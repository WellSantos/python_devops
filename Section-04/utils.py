#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import date

def escreverArquivo(nome,dados):
    with open("%s.txt"%nome,'w') as f:
        f.write(dados)

def lerArquivo(nome):
    with open("%s.txt"%nome,'r') as f:
        var = f.read()
    return var

def dataAtual():
    return date.today()
