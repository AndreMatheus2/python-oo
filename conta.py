
class Conta:
    def __int__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Saldo é {} do titular {}'.format(self.saldo, self.titular))
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor