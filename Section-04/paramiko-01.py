#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko.client import SSHClient
import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("globoplay-prod-fe-01.cmaq25fe-133.cp.globoi.com",username="well",password="W3llgl0b0c0m-_")
stdin,stdout,stderr = client.exec_command("ls -la")

if stderr.channel.recv_exit_status() != 0:
    print "Error code=",stderr.channel.recv_exit_status(),"- Error message=",stderr.read()
else:
    print stdout.read()
