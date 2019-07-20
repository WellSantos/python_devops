#!/usr/bin/env python
# -*- coding: utf-8 -*-

carrinho = []
produto = {"nome":"Tenis","valor":100}

blackFriday = lambda x: x*2

print "Valor do produto:",blackFriday(produto["valor"])
print "Com desconto de 50%",produto["valor"]

# explicação melhor
# https://medium.com/@otaviobn/entendendo-as-fun%C3%A7%C3%B5es-lambda-no-python-cbe3c5abb179
