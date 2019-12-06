#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import requests

SERVER_ADDRESS = ('localhost', 8686)

def send_telegram(text: str):
    token = "1030368472:AAGctnsO69piEV1QXQcr-FK4L5920SBTJ0Q"
    url = "https://api.telegram.org/bot"
    channel_id = "@thistle_test"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')


while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))

    data = connection.recv(1024)
    print(str(data))
    send_telegram(data)

    connection.send(bytes('Your message send to Telegram!', encoding='UTF-8'))

    connection.close()
