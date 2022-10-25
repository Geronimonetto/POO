from contas import ContaPoupanca,ContaCorrente

cp = ContaPoupanca(1111,1111,0)
cp.depositar(10)
cp.sacar(5)

print("****************************")

cc = ContaCorrente(1111,1111,0,500)
cc.sacar(500)
cc.sacar(200)
cc.depositar(1000)