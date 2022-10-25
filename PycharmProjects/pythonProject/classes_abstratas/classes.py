from abc import ABC,abstractmethod


class Conta:
    def __init__(self,conta, agencia, saldo):
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico! ")

        self._saldo = valor

    def detalhes(self):
        print(f'Agência: {self.agencia}',end=" ")
        print(f'Conta: {self.conta}',end=" ")
        print(f'Saldo: {self.saldo}')

    def depositar(self,valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numérico! ")
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self,valor):
        pass
