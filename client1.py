#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

address_to_server = ('localhost', 8686)
print('server is running, please, press ctrl+c to stop')

while True:
  message = input ("Your message>> ")

  clients = socket.socket()
  clients.connect(address_to_server)
  clients.send(bytes(message, encoding='UTF-8'))
#  data = clients.recv(1024)
#  print(str(data))