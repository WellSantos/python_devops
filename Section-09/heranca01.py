#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Servidor:
    memoria = 1024
    disco = 50
    cpu = 1
    tipo = None

    def contratarMemoria(self,memoria):
        self.memoria += memoria

    def contratarCpu(self,cpu):
        self.cpu += cpu

    def contratarDisco(self,disco):
        self.disco += disco


class Cloud(Servidor):
    def __init__(self):
        self.memoria = 512
        self.cpu = 1
        self.disco = 50
        self.tipo = "Cloud"

dns = Cloud()

print "Servidor do tipo:",dns.tipo
print "  Memória Inicial",dns.memoria
print "  Disco Inicial",dns.disco
print "  CPU Inicial",dns.cpu

class Fisico(Servidor):
    def __init__(self):
        self.memoria = 4096
        self.cpu = 4
        self.disco = 1024
        self.tipo = "Físico"

dns = Fisico()

print "Servidor do tipo:",dns.tipo
print "  Memória Inicial",dns.memoria
print "  Disco Inicial",dns.disco
print "  CPU Inicial",dns.cpu

dns.contratarDisco(1024)

print "Disco Total do Servidor Físico",dns.disco