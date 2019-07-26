#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Servidor:
    memoria = None
    disco = None
    cpu = None

dns = Servidor()


dns.memoria = 2048
dns.disco = 50
dns.cpu = 2

print "O servidor possui: CPU %s, Memória: %s, Disco: %s GB"%(dns.cpu,dns.memoria,dns.disco)