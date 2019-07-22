#!/usr/bin/env python
# -*- coding: utf-8 -*-


#import utils #arquivo no mesmo diretório
from modulos import utils as calango #importa o arquivo de outro diretório e dá um alias pra ele

calango.escreverArquivo("dados","Esses é o conteúdo do arquivo.")

print calango.lerArquivo("dados")
print calango.dataAtual()
