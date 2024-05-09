class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque_diario = 1500
        self.saldo_saque_diario = self.limite_saque_diario
        self.saques_restantes = 3

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor}")
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor <= self.saldo_saque_diario and valor <= self.saldo and self.saques_restantes > 0:
            self.saldo -= valor
            self.saldo_saque_diario -= valor
            self.saques_restantes -= 1
            self.extrato.append(f"Saque: -R${valor}")
            print("Saque realizado com sucesso.")
        elif valor > self.saldo_saque_diario:
            print("Valor do saque excede o limite diário.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif self.saques_restantes <= 0:
            print("Número máximo de saques diários atingido.")

    def imprimir_extrato(self):
        print("Extrato:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo}")


sistema_bancario = SistemaBancario()


sistema_bancario.deposito(1000)
sistema_bancario.saque(500)
sistema_bancario.saque(800) 
sistema_bancario.deposito(2000)
sistema_bancario.saque(700)
sistema_bancario.saque(400)
sistema_bancario.saque(300)  

sistema_bancario.imprimir_extrato()