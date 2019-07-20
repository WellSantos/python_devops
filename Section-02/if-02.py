#!/usr/bin/env python
# -*- coding: utf-8 -*-

user = "well"
pwd = "123"


login = raw_input("Digite o login: ")
senha = raw_input("Digite a senha: ")

if (login == user) and (senha == pwd):
    print "Usuário autenticado com sucesso!"
    print "Seja bem vindo %s" %login
else:
    print "Acesso negado!"
