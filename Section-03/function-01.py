#!/usr/bin/env python
# -*- coding: utf-8 -*-

produtos = []

def cadastraProduto(item):
    global produtos
    produtos.append(item)

item = ""

def listaProdutos():
    global produtos
    for p in produtos:
        print p

while item <> "sair":
    item = raw_input("Qual o produto para cadastrar? ")
    cadastraProduto(item)
    print "Produto cadastrado com sucesso"
    listaProdutos()
