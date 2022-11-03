#O método mágico setattr toda vez que você configurar um atributo novo dentro da nossa classe
# ele vai ser chamado.


class Teste:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        #O setattr dessa forma armazena o valor que foi criado pelo atributo a classe.
        self.__dict__[key] = value

    def falar(self):
        print(self.nome)
    
a = Teste()
#Criando atributo pela instância
a.nome = "Geronimo"
a.falar()