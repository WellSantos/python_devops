#!/usr/bin/env python
# -*- coding: utf-8 -*-

#create user 'teste'@'localhost' identified by 'teste123456';

import sys

try:
    import MySQLdb
except:
    sys.exit("[!] Por favor, instale a biblioteca mysqldb com o comando: sudo apt-get install python-mysqldb")

try:
    con = MySQLdb.connect(host="127.0.0.1", user="teste",db="projeto",passwd="teste123456")
    cur = con.cursor()
    cur.execute("insert into cliente(id,nome,cpf) values('4','Janis','12345678900')")
    con.commit()
    print "Registro criado com sucesso"

except Exception as e:
    print "Erro: %s"%e
finally:
    print "Finalizando a conexão com o banco de dados"
    cur.close()
    con.close()
