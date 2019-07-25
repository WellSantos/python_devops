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
db.fila.insert({"_id":1,"serviço":"Intranet","status":0})
db.fila.insert({"_id":2,"serviço":"Website","status":0})
db.fila.insert({"_id":3,"serviço":"Backup","status":0})
db.fila.insert({"_id":4,"servidor":"192.168.0.1","nome":"Asterisk"})
db.fila.insert({"_id":5,"servidor":"192.168.0.2","nome":"FreeNas"})
db.fila.insert({"_id":6,"servidor":"192.168.0.3","nome":"pfSense"})

for r in db.fila.find():
    print r