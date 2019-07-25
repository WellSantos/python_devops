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
    cur.execute("select * from cliente")
    #print "Primeiro registro",cur.fetchone()
    print "Todos os registros",cur.fetchall()
    con.commit()
except Exception as e:
    print "Erro: %s"%e
finally:
    print "Finalizando conexão com o banco de dados"
    cur.close
    con.close


