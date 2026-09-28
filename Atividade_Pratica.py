class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # GETTERS
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    # SETTERS
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_ano(self, ano):
        if ano > 1885:
            self.__ano = ano
        else:
            print("Ano inválido!")

    def acao(self):
        return "Ação executada com sucesso"


# ----------------------------------

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, porta):
        super().__init__(marca, modelo, ano)
        self.__porta = porta
        self.__luz = "desligada"

    def get_porta(self):
        return self.__porta

    def get_luz(self):
        return self.__luz

    def acao(self):
        if self.__luz == "desligada":
            self.__luz = "ligada"
        else:
            self.__luz = "desligada"

        return f"Luz {self.__luz} com sucesso!"

    def abrir_porta(self):
        if self.__porta == "fechada":
            self.__porta = "aberta"
        else:
            self.__porta = "fechada"

        return f"Porta {self.__porta} com sucesso!"


# ----------------------------------

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, estado):
        super().__init__(marca, modelo, ano)
        self.__estado = estado

    def get_estado(self):
        return self.__estado

    def acao(self):
        return "BII-BII!!!"

    def empinar_moto(self):
        if self.__estado == "retornada":
            self.__estado = "empinada"
        else:
            self.__estado = "retornada"

        return f"Moto {self.__estado} com sucesso!"


# ----------------------------------

C1 = Carro("Toyota", "Corolla", 2022, "fechada")
M1 = Moto("Honda", "CB 600", 2023, "retornada")

print(C1.get_marca())
print(C1.acao())
print(C1.abrir_porta())

print(M1.get_modelo())
print(M1.acao())
print(M1.empinar_moto())
    
