#Sempre que usamos a função len com uma classe para fazer a contagem
# é como se tivessemos usando o método mágico __len__.

class Teste():

    def __init__(self,nome):
        pass

    def __len__(self):
        pass
    

a = Teste("nome")

#O valor do __len__ vai ser o valor que estiver dentro do método, porém é usado
#quando temos objetos dentro desse objeto a como por exemplo, listas, mostrando o valor
#de quantos objetos tem dentro da classe;

print(a.__len__())
