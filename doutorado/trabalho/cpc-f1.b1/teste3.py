import matplotlib.pyplot as plt
import xarray as xr

# 1. Abre o arquivo NetCDF
d_seco = xr.open_dataset("maoaafcpcF1.b1.20140222.143709.nc")
d_umid = xr.open_dataset("maoaafcpcF1.b1.20140909.150111.nc")

# 2. Seleciona a variável concentration
Na_seco = d_seco["concentration"]
Na_umid = d_umid["concentration"]

# 3. Configura o tamanho da figura (Largura x Altura)
plt.figure(figsize=(10, 5))

# 4. Plota os dados (o xarray define o eixo X como o Tempo automaticamente)
Na_seco.plot(marker="o", color="orange", linestyle="-")

# 5. Customização visual do gráfico
plt.title("Evolução de Na no período seco", fontsize=14, pad=15)
plt.xlabel("Tempo", fontsize=12)
plt.ylabel(
    f"Na ({Na_seco.attrs.get('units', 'u.m.')})", fontsize=12
)
plt.grid(True, linestyle="--", alpha=0.6)

# 6. Rotaciona as datas do eixo X para não sobrepor
plt.xticks(rotation=45)
plt.tight_layout()

# 3. Configura o tamanho da figura (Largura x Altura)
plt.figure(figsize=(10, 5))

# 4. Plota os dados (o xarray define o eixo X como o Tempo automaticamente)
Na_umid.plot(marker="*", color="blue", linestyle="-")


# 5. Customização visual do gráfico
plt.title("Evolução de Na no período úmido", fontsize=14, pad=15)
plt.xlabel("Tempo", fontsize=12)
plt.ylabel(
    f"Na ({Na_umid.attrs.get('units', 'u.m.')})", fontsize=12
)
plt.grid(True, linestyle="--", alpha=0.6)

# 6. Rotaciona as datas do eixo X para não sobrepor
plt.xticks(rotation=45)
plt.tight_layout()

# 7. Exibe o gráfico
plt.show()