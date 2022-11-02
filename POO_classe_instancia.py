class AnoAniversario:

    numero = int(input("Digite o número: "))


    def _init_(self,first_number):
        self.__first_number = first_number


    @property
    def fisrt_number(self):
        return self.__first_number


    @fisrt_number.setter
    def first_number(self,valor):
        if isinstance(valor,str):
            valor = int(valor)
        self.__first_number = valor


    def tabuada(self):
        for v in range(10):
            v +=1
            soma = self.first_number + v
            print(f"{self.first_number} + {v} = {soma}")

    @staticmethod
    def mensagem():
        print("--"*10)
        print("Bem vindo a TABUADA".center(20))
        print("--"*10)




obj1 = AnoAniversario(AnoAniversario.numero)
obj1.mensagem()
obj1.tabuada()