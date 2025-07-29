# DESAFIO

# Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementaras seguintes funcionalidades no sistema:

# Estabelecer um limite de 10 transações diárias para uma conta
# Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia
# mostre no extrato a data e hora de todas as transações

from datetime import datetime, date

# Classe para representar uma conta bancária
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.transacoes = []  # Lista para armazenar as transações (valor, data e hora)
        self.limite_diario = 10  # Limite de 10 transações por dia

    def pode_transacionar(self):
        """Verifica se ainda há transações disponíveis para o dia atual"""
        hoje = date.today()
        # Conta quantas transações ocorreram hoje
        transacoes_hoje = [t for t in self.transacoes if t["data"].date() == hoje]
        return len(transacoes_hoje) < self.limite_diario

    def realizar_transacao(self, valor):
        """Realiza uma transação caso o limite diário não tenha sido atingido"""
        if not self.pode_transacionar():
            print("❌ Limite diário de transações atingido!")
            return

        agora = datetime.now()  # Data e hora atuais
        self.transacoes.append({
            "valor": valor,
            "data": agora
        })
        print(f"✅ Transação de R${valor:.2f} realizada em {agora.strftime('%d/%m/%Y %H:%M:%S')}")

    def extrato(self):
        """Exibe todas as transações com data e hora"""
        if not self.transacoes:
            print("📄 Nenhuma transação registrada.")
            return

        print(f"\n📜 Extrato de {self.titular}:")
        for t in self.transacoes:
            data_formatada = t["data"].strftime('%d/%m/%Y %H:%M:%S')
            print(f" - R${t['valor']:.2f} em {data_formatada}")


# ==== EXEMPLO DE USO ====
conta = Conta("João Silva")

# Simulando 11 transações para testar o limite
for i in range(11):
    conta.realizar_transacao(100 + i)

# Exibir extrato final
conta.extrato()
