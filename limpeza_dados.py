# ============================================
# PROJETO: Limpeza de Dados de Clientes
# Autor: Thiago Rodrigues
# Ferramentas: Python, Pandas
# ============================================

import pandas as pd

# ── 1. CRIANDO UMA BASE DE DADOS FICTÍCIA ──
# (simula uma planilha bagunçada do mundo real)

dados = {
    "nome":   ["Ana Silva", "Carlos Lima", "Ana Silva", "pedro souza", "maria santos", None],
    "idade":  [25, None, 25, -5, 30, 22],
    "cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", None, "são paulo", "Curitiba"],
    "salario":[3000, 5000, 3000, 2000, None, 4000]
}

df = pd.DataFrame(dados)

print("=== DADOS ORIGINAIS ===")
print(df)
print()

# ── 2. DIAGNÓSTICO ──
print("=== VALORES VAZIOS POR COLUNA ===")
print(df.isnull().sum())
print()

# ── 3. REMOVER DUPLICATAS ──
df = df.drop_duplicates()
print(f"Linhas após remover duplicatas: {len(df)}")

# ── 4. PREENCHER VALORES VAZIOS ──
df["idade"]   = df["idade"].fillna(df["idade"].mean())
df["salario"] = df["salario"].fillna(df["salario"].mean())
df["cidade"]  = df["cidade"].fillna("Desconhecida")
df["nome"]    = df["nome"].fillna("Desconhecido")

# ── 5. CORRIGIR IDADES INVÁLIDAS ──
df = df[df["idade"] >= 0]

# ── 6. PADRONIZAR TEXTO ──
df["nome"]   = df["nome"].str.title()
df["cidade"] = df["cidade"].str.title()

# ── 7. RESULTADO FINAL ──
print()
print("=== DADOS LIMPOS ===")
print(df)
