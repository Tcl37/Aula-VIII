class veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
class carro(veiculo):
    def __init__(self,marca,modelo,ano,porta):
        self.porta = porta
    def abrir_porta(self):
class moto(veiculo):
    def __init__(self,marca,modelo,ano,estado):
        self.estado = estado
    def empinar(self):
        self.estado = empinado
