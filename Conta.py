"""Local onde é realizado as operações do banco"""
from msilib.schema import Property
"""CRIA A PARTE BÁSICA DO BANCO(Dados do usuário)"""
class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = float(saldo)
"""Código do depósito"""
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido para depósito")
"""Código do saque da conta"""
    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Valor inválido para saque ou saldo insuficiente")
"""Código do extrato da conta"""
    def extrato(self, extrato):
        self.extrato = extrato
        if extrato > 0:
            self.extrato = self.saldo - self.extrato
            print(f"Saldo atual: R${self.saldo:.2f}")
            print(f"Saldo Pós saque: R${self.extrato:.2f}")
"""Retorno dos dados da conta"""
    def __str__(self):
        return f"Conta: {self.numero}, Titular: {self.titular}, Saldo: R${self.saldo:.2f}"
