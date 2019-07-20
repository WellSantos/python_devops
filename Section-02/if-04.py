#!/usr/bin/env python
# -*- coding: utf-8 -*-

so = input("Qual o melhor sistema operacional?\n"
                "1 - Linux\n"
                "2 - Windows\n"
                "3 - Mac\n"
                "Digite sua resposta: ")


if so == 1:
    print "Linux é o melhor s.o. do mundo"
elif so == 2:
    print "O Windows é muito bugado"
elif so == 3:
    print "Mac é um Windows mais bonitinho"
else:
    print "Opção inválida"
