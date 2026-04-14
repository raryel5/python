import pandas as pd

# Exemplo de duas séries de dados
data = {
    'variavel_a': [10, 20, 30, 40, 50],
    'variavel_b': [15, 25, 35, 45, 55]
}
df = pd.DataFrame(data)

# Calcular correlação de Pearson (padrão)
correlacao = df['variavel_a'].corr(df['variavel_b'])
print(f"Correlação: {correlacao}")