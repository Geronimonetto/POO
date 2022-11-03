#Recriando a função open() para criar arquivos.

class Escrever:

    def __init__(self,escrever,modo):
        self.escrever = open(escrever,modo)

    def __enter__(self):
        return self.escrever
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.escrever.close()
        # As exc_type,exc_val,exc_tb serão executadas apenas se encontrar um erro 
        # ou seja vai aparecer o tipo de exceção, valor da exceçao,e o traceback da exceção.
        # o que podemos fazer é tratar a exceção aqui dentro e ao final dar um return True
        return True
        
with Escrever("Arquivo.txt","w") as escrever:
    #Usamos o apelido para chamar as funçoes dentro do open assim como no novo metodo.
    escrever.write('Meu nome é geronimo')

#Funciona como uma sobrescrição mas o open continua funcionando normalmente.
with open("Novoarquivo.txt","w") as arquivo:
    arquivo.write("Estou funcionando do mesmo jeito.")

    #Exceção feita propositalmente.
    arquivo.auhduahduahdu("Exceção encontrada")
