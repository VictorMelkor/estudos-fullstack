# 1. 👤 Pessoa e Aluno (Herança)
# Objetivo: Modelar uma classe Pessoa com atributos básicos e uma classe Aluno que herda Pessoa adicionando matrícula

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

# Exemplo de uso
a1 = Aluno("Victor", 25, "A001")
print(a1.nome)       # Herdado de Pessoa
print(a1.matricula)  # Atributo próprio


# ---


# 🏦 ContaBancaria
# Objetivo: Modelar uma conta bancária com métodos básicos: depositar, sacar e extrato

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: R${self._saldo:.2f}")

# Exemplo de uso
c1 = ContaBancaria("Victor", 500)
c1.depositar(200)
c1.sacar(100)
c1.extrato()  # Saldo: R$600.00


# ---


# 🖨️ Sobrescrevendo __str__
# Objetivo: Tornar a impressão de objetos mais clara e amigável com __str__

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f}"

# Exemplo de uso
p = Produto("Café", 12.5)
print(p)
# Saída: Produto: Café | Preço: R$12.50
