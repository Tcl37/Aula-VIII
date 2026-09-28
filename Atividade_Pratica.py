class veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
class carro(veiculo):
    def __init__(self,marca,modelo,ano,porta):
        self.porta = porta
    def abrir_porta(self):