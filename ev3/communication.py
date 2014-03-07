# -*- coding: utf-8 -*-
import socket


class Communication(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, addr, port):
        self._socket.connect((addr, port))

    def send(self, data):
        self._socket.send(data)

    def receive(self, length):
        return self._socket.recv(length)

    def close(self):
        self._socket.close()