
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo é {} do titular {}'.format(self.__saldo, self.__titular))
    def deposita(self, valor):
        self.__saldo += valor

    def __podeSacar(self, valorSacar):
        valorDisponivel = self.__saldo + self.__limite
        return valorSacar <= valorDisponivel
    def saca(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite