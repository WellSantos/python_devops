#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    import psycopg2
except:
    sys.exit("[!] Por favor, instale a biblioteca psycopg2 com o\
    comando: sudo apt-get install python-psycopg2")

try:
    con = psycopg2.connect("host=127.0.0.1 dbname=projeto user=admin password=123456")
    cur = con.cursor()
    cur.execute("update cliente set nome='Verônica' where id=2")
    print "Atualização executada com sucesso"
    cur.execute('delete from cliente where id=01')
    print "Remoção realizada com sucesso"
    con.commit()
except Exception as e:
    print "Erro: %s"%e
    print "Fazendo rollback"
    con.rollback()
finally:
    print "Finalizando conexão com o banco de dados"
    cur.close
    con.close
