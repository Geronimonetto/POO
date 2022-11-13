# Praticando Decoradores Getters e Setters

class Metodo:
    valor = 10
    def __init__(self,nome,preco):
        self.__nome = nome
        self.__preco = preco
    
    @property  # Pegando o objeto de instancia nome (Getter)
    def nome(self):
        return self.__nome

    @nome.setter  # Alterando o objeto de instância (Setter)
    def nome(self,novo_nome):
        if isinstance(novo_nome,str):
            novo_nome = novo_nome.replace("n","N")
        self.__nome = novo_nome

    @property  # Pegando o objeto de instância preco (Getter)
    def preco(self):
        return self.__preco

    @preco.setter  # Alterando o objeto de instância (Setter)
    def preco(self,novo_preco):
        if isinstance(novo_preco,int):
            novo_preco = float(novo_preco)
        self.__preco = novo_preco

    def validando(self):
        print(f"estou printando {self.preco} ")


variavel = Metodo("nome",2)
variavel.validando()