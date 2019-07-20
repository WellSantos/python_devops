#!/usr/bin/env python
# -*- coding: utf-8 -*-

users = []
nome = ""

while nome != "sair":
    nome = raw_input("Digite o nome(ou sair): ")
    if nome == "sair":
        print "Saindo do chat"
        break
    if not nome in users:
        print nome+" entrou no chat"
        users.append(nome)
    for u in users:
        print u+" está online"

#outros comandos para manipulação de listas
animais = ["cachorro","gato","passarinho"] #lista

animais.append("boi") #add ao final da lista
animais.insert(2,"boi") #add na posição da lista
animais.remove("boi") #remove da lista
animais.pop() #remove o último da lista
animais.pop(1) #remove da posição 1 da lista
animais.count("boi") #mostra quantos itens(boi) tem na lista
animais.index("gato") #mostra a posição do item(gato) na lista
