#O método __str__ é chamado sempre que eu tentar chamar minha classe como uma string

class Teste:

    def __init__(self):
        pass

    def __str__(self):
        return "Estou usando esse método pois vou usar o print"


objeto = Teste()

#Imprimindo a instância da classe, se o metodo __str__ não estivesse na classe o resultado seria assim:
#<__main__.Teste object at 0x0000019A9B75B100>
print(Teste())
#Acontece o mesmo com a instância
print(objeto)