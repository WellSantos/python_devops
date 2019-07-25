#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    from pymongo import MongoClient
except:
    sys.exit("[!] Por favor, instale a biblioteca pymongo com o comando: sudo apt install python-pymongo")


client = MongoClient("127.0.0.1")
db = client["devops"]

db.fila.remove()

servidor1 = {"endereco":"192.168.0.1","nome":"dns"}
servidor2 = {"endereco":"192.168.0.2","nome":"postgres"}

servidores = []

servidores.append(servidor1)
servidores.append(servidor2)

db.fila.insert({"_id":1,"analista":"Well","servidores":servidores})

for r in db.fila.find():
    print "O analista:",r['analista'],"tem acesso aos servidores"
    for s in r['servidores']:
        print s['nome']," - ",s['endereco']
