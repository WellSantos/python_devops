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

def totalCarrinho(carrinho):
    return sum(produto["valor"] for produto in carrinho)

def cupomDesconto(cupom=""):
    if cupom == "gratis":
        return 0.70
    else:
        return 1

print "O total da sua compra é de:",(totalCarrinho(carrinho)*cupomDesconto())
print "Usando o cupom \"gratis\", o total é de:",(totalCarrinho(carrinho)*cupomDesconto("gratis"))
