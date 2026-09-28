class ContaBancaria:
    def __init__(self,titular,saldo_inicial):
        self.titular = titular
        self.__saldo = 0
        self.definir_saldo(saldo_inicial)
    def obter_saldo(self):
        return self.__saldo

    def transferir(self,valor,conta_destino):
        if valor <= 0:
            print("Erro: O valor da transferência deve ser maior que zero.")
        elif valor > self.__saldo:
            print(f"Erro: Saldo insuficiente. Saldo atual é R${self.saldo}.")
        else:
            self.__saldo -= valor
            conta_destino.__saldo += valor
            print(f"Transferência de R${valor} para {conta_destino.titular}")
conta_ana = ContaBancaria("Ana",1000)
conta_Bruno = ContaBancaria("Bruno",200)
conta_ana.transferir(300,conta_Bruno)
print(f"Saldo da Ana: R${conta_ana.__saldo}")
print(f"Saldo do Bruno: R${conta_Bruno.__saldo}")
conta_ana.transferir(800,conta_Bruno)
#Erro saldo insuficiente,R$700.