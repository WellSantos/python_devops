#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Servidor:
    memoria = 1024
    disco = 50
    cpu = 1

    def contratarMemoria(self,memoria):
        self.memoria += memoria

    def contratarCpu(self,cpu):
        self.cpu += cpu

    def contratarDisco(self,disco):
        self.disco += disco

dns = Servidor()


dns.contratarMemoria(1024)
dns.contratarCpu(3)
dns.contratarDisco(50)

print "O servidor possui: CPU %s, Memória: %s, Disco: %s GB"%(dns.cpu,dns.memoria,dns.disco)