#Quando queremos criar uma docstrings de apenas uma linha devemos criar no início do módulo.

#exemplo:

#import modulo from uma_linha

"""Essa é a documentação de uma linha"""


#___________________________________________________________________________________________________________________________________________________________

# Criando uma Dosctrings longa

"""Aqui fica a o name

aqui fica a descrição- Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
 It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in 
 the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
 PageMaker including versions of Lorem Ipsum.


"""

valor = 'valor1'

def func(x,y):
    """Descrição da função está aqui dentro
        Essa função multiplica x e y
    """
    return x*y
# quando damos um help(modulo) vemos tudo que existe dentro do modulo
# quando damos um help em uma func específica vemos o que está dentro daquela função Ex: help(func)
