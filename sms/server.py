from abc import ABCMeta, abstractmethod
import time


class Server(metaclass=ABCMeta):

    def __init__(self, sign, content, phones):
        self.sign = sign
        self.content = content
        self.phones = phones

    @abstractmethod
    def send_sms(self):
        pass


class AliServer(Server):

    def send_sms(self):
        return True
