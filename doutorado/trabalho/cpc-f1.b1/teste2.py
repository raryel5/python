import matplotlib.pyplot as plt
import xarray as xr

# 1. Abre o arquivo e seleciona a variável
ds = xr.open_dataset("maoaafcpcF1.b1.20140222.143709.nc")
concentracao = ds["qc_concentration"]

# 2. Se os dados forem 3D (time, lat, lon), selecionamos um ponto específico
if len(concentracao.dims) > 1:
    # Seleciona o ponto mais próximo da lat/lon desejada
    serie_temporal = concentracao.sel(lat=-23.5, lon=-46.6, method="nearest")
else:
    serie_temporal = concentracao

# 3. Plota o gráfico de linha
serie_temporal.plot(marker="o", color="blue")
plt.title("Variação da Concentração ao Longo do Tempo")
plt.grid(True)
plt.show()