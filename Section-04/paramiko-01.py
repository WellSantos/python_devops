#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko.client import SSHClient
import paramiko

key_path = "/Users/well/.ssh/id_rsa"
host = "globoplay-prod-fe-01.cmaq25fe-133.cp.globoi.com"

client = SSHClient()
key = paramiko.RSAKey.from_private_key_file(key_path)
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print "Connecting to host: "+host
client.connect(host,username="well",pkey=key)
print "Connected"
stdin,stdout,stderr = client.exec_command("ls -la && echo && whoami")

if stderr.channel.recv_exit_status() != 0:
    print "Error_code=",stderr.channel.recv_exit_status(),"- Error_message=",stderr.read()
else:
    print stdout.read()

client.close()
