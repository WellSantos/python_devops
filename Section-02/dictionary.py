#!/usr/bin/env python
# -*- coding: utf-8 -*-

carrinho = []

produto1 = {"nome":"tenis","valor":59.90}
produto2 = {"nome":"meia","valor":9.90}
produto3 = {"nome":"short","valor":19.90}
produto4 = {"nome":"camisa","valor":39.90}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)

print "Seu carrinho possui",len(carrinho),"itens."

total=0

for c in carrinho:
    total += c["valor"]
print "O valor total é de:",total
