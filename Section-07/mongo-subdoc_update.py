#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    from pymongo import MongoClient
except:
    sys.exit("[!] Por favor, instale a biblioteca pymongo com o comando: sudo apt install python-pymongo")


client = MongoClient("127.0.0.1")
db = client["devops"]

db.fila.update({"_id":1,"servidores.nome":"dns"},{"$pull":{"servidores":{"nome":"dns"}}})
db.fila.update({"_id":1},{"$addToSet":{"servidores":{"nome":"powerdns","endereco":"192.168.30.1"}}})




for r in db.fila.find():
    print "O analista:",r['analista'],"tem acesso aos servidores"
    for s in r['servidores']:
        print s['nome']," - ",s['endereco']