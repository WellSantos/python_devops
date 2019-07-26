#!/usr/bin/env python
# -*- coding: utf-8 -*-

from servidor import Servidor
from acesso import Acesso

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
                print "Total de Slots",self.total_slots
                print "Total Ocupados",self.slots_ocupados
        else:
            print "Tamanho de disco não é válido"

    def acessarConsole(self):
        print "Acesso por IPMI"


dns = Fisico()
dns.acessarConsole()