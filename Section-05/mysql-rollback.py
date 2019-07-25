#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    import MySQLdb
except:
    sys.exit("[!] Por favor, instale a biblioteca mysqldb com o comando: sudo apt-get install python-mysqldb")

try:
    con = MySQLdb.connect(host="127.0.0.1", user="teste",db="projeto",passwd="teste123456")
    cur = con.cursor()
    cur.execute("update cliente set cnome='Verônica' where id=2")
    print "Atualização executada com sucesso"
    con.commit()
except Exception as e:
    print "Erro: %s"%e
    print "Fazendo rollback"
    con.rollback()
finally:
    print "Finalizando conexão com o banco de dados"
    cur.close
    con.close
