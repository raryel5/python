import matplotlib.pyplot as plt
import xarray as xr

# 1. Abre o arquivo NetCDF
ds = xr.open_dataset("maoaafcpcF1.b1.20140301.133308.nc")

# 2. Seleciona a variável concentration
concentracao = ds["concentration"]

# 3. Configura o tamanho da figura (Largura x Altura)
plt.figure(figsize=(10, 5))

# 4. Plota os dados (o xarray define o eixo X como o Tempo automaticamente)
concentracao.plot(marker="o", color="darkcyan", linestyle="-")

# 5. Customização visual do gráfico
plt.title("Evolução da Concentração ao Longo do Tempo", fontsize=14, pad=15)
plt.xlabel("Tempo", fontsize=12)
plt.ylabel(
    f"Concentração ({concentracao.attrs.get('units', 'u.m.')})", fontsize=12
)
plt.grid(True, linestyle="--", alpha=0.6)

# 6. Rotaciona as datas do eixo X para não sobrepor
plt.xticks(rotation=45)
plt.tight_layout()

# 7. Exibe o gráfico
plt.show()