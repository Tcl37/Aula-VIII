class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo

conta = ContaBancaria("Ana", 1000)
print(conta.titular)
print(conta.get_saldo())