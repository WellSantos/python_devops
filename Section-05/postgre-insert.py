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
    cur.execute("insert into cliente(id,nome,cpf) values(3,'Wellington','123.456.789-00')")
    con.commit()
    print "Registro criado com sucesso"
except Exception as e:
    print "Erro: %s"%e
    print "Fazendo rollback"
    con.rollback()
finally:
    print "Finalizando conexão com o banco de dados"
    cur.close
    con.close


