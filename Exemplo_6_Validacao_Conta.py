class ContaBancaria:
    def __init__(self,titular,saldo_inicial):
        self.titular = titular
        self.__saldo = 0
        self.definir_saldo(saldo_inicial)
    def obter_saldo(self):
        return self.__saldo
    def definir_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Erro: O saldo não pode ser negativo!")
    def sacar(self,valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser maior do que zero.")
        elif valor > self.__saldo:
            print("Erro: Saldo insuficiente para realizar o saque.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} realiado com sucesso!")
minha_conta = ContaBancaria("Carlos",500)
minha_conta.definir_saldo(-100) #Saldo não pode ser negativo
minha_conta.sacar(600) #Saldo insuficiente
