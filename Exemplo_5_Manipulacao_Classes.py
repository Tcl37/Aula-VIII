class Produto:
    def __init__(self, nome,preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, precentual):
        self.preco -= self.preco * (percentual / 100)

produto1 = Produto("Notebook", 4500)

print(produto1.nome,"-",produto1.preco)
produto1.aplicar_desconto(10)
print("Após desconto:", produto1.nome,"-",produto1.preco)

setattr(produto1, "categoria","Informática") #Adiciona um atributo
print("Categoria:", getattr(produto1,"categoria"))