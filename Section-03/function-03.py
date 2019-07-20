#!/usr/bin/env python
# -*- coding: utf-8 -*-

servidor = "192.168.0.1"

def alteraServidor(ip):
    global servidor
    servidor = ip

print "O servidor atual é o",servidor
ip = raw_input("Qual o ip do novo servidor? ")
alteraServidor(ip)
print "O novo servidor é",servidor
