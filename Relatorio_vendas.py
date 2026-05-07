import pandas as pd

# ── 1. CARREGAR OS DADOS ──
dados = {
    "vendedor": ["Ana","Carlos","Ana","Pedro","Carlos","Pedro"],
    "produto":  ["Notebook","Mouse","Teclado","Notebook","Monitor","Mouse"],
    "valor":    [3500, 150, 300, 3500, 1200, 150],
    "status":   ["concluido","cancelado","concluido","concluido","concluido","cancelado"]
}

df = pd.DataFrame(dados)

# ── 2. REGRA DE NEGÓCIO ──
# Só conta vendas concluídas!
df_valido = df[df["status"] == "concluido"]

# ── 3. TOTAL DE VENDAS ──
total = df_valido["valor"].sum()
print(f"Total de vendas: R$ {total}")

# ── 4. VENDAS POR VENDEDOR ──
por_vendedor = df_valido.groupby("vendedor")["valor"].sum()
print("\nVendas por vendedor:")
print(por_vendedor)

# ── 5. PRODUTO MAIS VENDIDO ──
mais_vendido = df_valido["produto"].value_counts().idxmax()
print(f"\nProduto mais vendido: {mais_vendido}")

# ── 6. TICKET MÉDIO ──
ticket_medio = df_valido["valor"].mean()
print(f"Ticket médio: R$ {ticket_medio:.2f}")
