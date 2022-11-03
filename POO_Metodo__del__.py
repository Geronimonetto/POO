# O método __del__ na teoria funciona da seguinte forma, quando chega ao fim do uso do objeto 
# ele é coletado.

class Teste:

    def __init__(self):
        pass

    def __del__(self):
        print("Objeto Coletado.")


test = Teste()
#Aqui quando encerrar o objeto test é coletado.