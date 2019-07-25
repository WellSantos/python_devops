#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    from pymongo import MongoClient
except:
    sys.exit("[!] Por favor, instale a biblioteca pymongo com o comando: sudo apt install python-pymongo")


client = MongoClient("127.0.0.1")
db = client["devops"]

db.fila.update({"_id":2},{"$set":{"serviço":"Linux"}})
db.fila.update({"_id":4},{"$set":{"servidor":"192.168.0.100"}})

for r in db.fila.find():
    print r