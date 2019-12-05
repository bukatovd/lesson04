#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

address_to_server = ('localhost', 8686)

clients = socket.socket()
clients.connect(address_to_server)
clients.send(str("hello"))

data = clients.recv(1024)
print(str(data))