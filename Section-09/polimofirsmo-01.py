#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heranca01 import Servidor

class Fisico(Servidor):
    def __init__(self):
        self.memoria = 4096
        self.cpu = 4
        self.disco = 1024
        self.tipo = "Físico"
        self.total_slots = 4
        self.slots_ocupados = 1

    def contratarDisco(self,disco):
        if disco == 500 or disco == 1024:
            if self.total_slots > self.slots_ocupados:
                self.slots_ocupados += 1
                self.disco += disco
            else:
                print "Você não possui mais slots disponíveis"
                    

dns = Fisico()

print "  Memória Inicial",dns.memoria
print "  Disco Inicial",dns.disco
print "  CPU Inicial",dns.cpu

dns.contratarDisco(1024)
dns.contratarDisco(1024)
# dns.contratarDisco(1024)
# dns.contratarDisco(1024)

print "Disco Total",dns.disco