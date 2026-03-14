# Exercício de conta bancária

class Conta:
    """
    A classe Conta executa operações de depósito e saque. Para utiliza-la escreva:
    Pessoa = Conta(id, nomePessoa, saldo)
    Inserir o saldo na criação é opcional.
    Por meio dos métodos saque() e deposito() você pode sacar e depositar valores.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} foi criada com sucesso. Saldo atual: R$ {self.saldo:,.2f}.")

    def deposito(self, quantia):
        saldoAnterior = self.saldo
        self.saldo += quantia
        print(f"Saldo anterior: R$ {saldoAnterior:,.2f};\nSaldo atual: R$ {self.saldo}.")

    def saque(self, quantia):
        if quantia > self.saldo:
            print("Operação cancelada. Valor maior que o saldo disponível.")
        else:
            self.saldo -= quantia
            print(f"Quantia solicitada: R$ {quantia:,.2f};\nSaldo final: {self.saldo:,.2f}.")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem saldo de R$ {self.saldo:,.2f}."


Mauro = Conta(1, "Mauro")

Mauro.deposito(5000)
# Mauro.saque(350)
# Mauro.saque(100000)
print(Mauro)

print(Conta.__doc__)

