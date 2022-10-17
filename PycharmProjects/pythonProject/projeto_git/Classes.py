from nova_classe import msg,modelando,todas,valor


class dinheiro:

    def __init__(self):
        msg()

    def menu(self):
        self.real = float(input("Valor em R$: "))
        modelando(todas)
        self.converter = float(input("Converter para: "))
        self.alterar()

    def alterar(self):
        if self.converter == 1:
            print(f'O valor R${self.real:.2f} em US$ (Dólares) = US${self.real * valor[0]:.2f}'.replace('.',','))

        elif self.converter == 2:
            print(f'O valor R${self.real:.2f} em £ (libra) = £{self.real * valor[1]:.2f}'.replace('.',','))

        elif self.converter == 3:
            print(f'O valor R${self.real:.2f} em ¥ (Iene) = ¥{self.real * valor[2]:.2f}'.replace('.',','))

        elif self.converter == 4:
            print(f'O valor R${self.real:.2f} em ¥ (Iene) = ¥{self.real * valor[2]:.2f}'.replace('.',','))
        self.menu()




