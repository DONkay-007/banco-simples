"""Bloco de código responsável pelo funcionamento do banco"""
class Main:
    from Cliente import Cliente
    from Conta import Conta

    print("Testando projeto")

    C1 = Cliente("João", "114444-2222")
    print(C1)
    print(C1.nome, "é", C1.telefone)

    banco = Conta("Luis", "223", 6000)
    print(banco)
    print("O senhor", banco.titular, "de número:", banco.numero, "tem na sua conta um saldo de R$:", banco.saldo) 

     """Parte responsável por fazer as operações no Banco"""
     
    banco.deposito(1000)
    banco.saque(150)
    banco.extrato(500)

    print(banco.deposito)
    print(banco.saque)
    print(banco.extrato)
