#!/usr/bin/env python
# -*- coding: utf-8 -*-

servers = ["dns","ldap","webserver","database","mongo"]

for s in servers:
    if s == "webserver":
        print "Atualização não pode ser executada",s
        continue
    else:
        print "Atualizado - ",s
