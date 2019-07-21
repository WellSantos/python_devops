#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

acesso = datetime(2019,07,21,00,00,00)
atual = datetime(2019,07,21,01,00,00)

if (atual - acesso).total_seconds() > 3600:
    print "Token expirado"
else:
    print "Acesso autorizado"
