class Teste:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    
obj = Teste("Geronimo",2)
#Modificando Valores nome e idade da classe
Teste.nome = "Novonome"
Teste.idade = 50

obj.nome = "Luiz"
obj.idade = 22
#valores apenas modificados na instância
print(obj.nome,obj.idade)

#Valores modificados na própria classe
print(Teste.nome,Teste.idade)
obj2 = Teste("amor",30)
print(Teste.nome,Teste.idade)
print(obj2.nome,obj2.idade)