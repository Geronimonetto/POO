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