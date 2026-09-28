class Funcionario:
    def _init_(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def detalhes(self):
            return f"Funcinário: (self.nome), Salário: R$:(self.salario)"

class Gerente(Funcionario): #HERANÇA
    def _init_(self,nome,salario,setor):
        super()._init_(nome,salario)
        self.setor = setor
    def detalhes(self): #POLIMORFISMO
        return f"Gerente: (self.nome), Salário: R$:(self.salario), Setor: (self.setor)"
G1 = Gerente("Dantas",5000,3)
print(G1.detalhes())
