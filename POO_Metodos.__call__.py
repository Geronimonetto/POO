#Os métodos mágicos são algumas funcionalidades que podemos usar em nossas classes 
#Fazendo com que elas se comportem de forma diferente ou obtenham algum outra melhoria

class A:
    #construtor
    def __init__(self):
        pass

    def __call__(self, *args, **kwds):
        #Criando variável dentro do metodo call
        valor = 1   
        
        #iterando sobre os parametros args que vou passar
        for v in args:
            valor += v
        return valor

    #Criando um metodo normal
    def falando(self):
        print("Estou funcionando tbm da mesma forma.")


a = A()
valor = a(1,2,3,4,5,96)
a.falando()
print(valor)