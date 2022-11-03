from contextlib import contextmanager

@contextmanager # usando o decorador context manager
def criar(arquivo,modo):  #criando a função com o nome do gerenciador 

    #Escopo da criação do gerenciador
    try:
        arquivo = open(arquivo,modo)

        #não podemos dar um return se não não irá chegar no finally
        yield arquivo

    #finally sempre vai passar por aqui, fechando arquivo.
    finally:
        arquivo.close()
    
#sempre deve ser chamado com o with se não vai encontrar um erro.
with criar("Abc.txt","w") as criando:
    criando.write("Criando arquivo.")