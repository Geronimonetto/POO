"""
Quero criar um Animal

Animal - uma classe ( podendo ser abstrata, a base) -> metodo respirar (é um animal)
	
	- Do animal quero criar um lobo(herdando de animal) - tudo que tem em animal tem em lobo - logo também herda o metodo respirar, se criar uivar aqui na classe lobo, a classe 
    animal não tem o metodo uivar. ( lobo é um lobo e também é um animal)
	
	- Quero criar mais específico cachorro( herda de lobo) - cachorro também recebe respirar - cachorro também 
    tem o metodo uivar, criado metodo cachorro aqui dentro nenhuma das classes acima recebe o metodo latir.(cachorro é um cachorro, um lobo e um animal.)



"""


#Bibliotecas
class Bibliotecas:  #Classe Pai
    def chama_metodo_interface(self):
        self.metodo_da_interface()  # isso so da certo por que o self - está ligado a instancia e com isso verifica que o metodo existe.

    

#interface
class interface(Bibliotecas):  #herdando da classe Bibliotecas
    def metodo_da_interface(self):
        print("Sou o metodo da interface!")



#main

instancia = interface()
instancia.chama_metodo_interface()