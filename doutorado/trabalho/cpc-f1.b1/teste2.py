import matplotlib.pyplot as plt
import xarray as xr

# 1. Abre o arquivo e seleciona a variável
# ds = xr.open_dataset("maoaafcpcF1.b1.20140222.143709.nc")
d_seco = xr.open_mfdataset("seco/*.nc", combine="by_coords")
d_umid = xr.open_mfdataset("umido/*.nc", combine="by_coords")
conc_seco = d_seco["qc_concentration"]
conc_umid = d_umid["qc_concentration"]

# 2. Se os dados forem 3D (time, lat, lon), selecionamos um ponto específico
if len(conc_seco.dims) > 1:
    # Seleciona o ponto mais próximo da lat/lon desejada
    serie_temporal = conc_seco.sel(lat=-23.5, lon=-46.6, method="nearest")
else:
    serie_temporal = conc_seco

# 3. Plota o gráfico de linha
plt.figure(figsize=(10, 5))
serie_temporal.plot(marker="o", color="blue")
plt.title("Variação da Concentração ao Longo do Tempo")
plt.grid(True)

# 2. Se os dados forem 3D (time, lat, lon), selecionamos um ponto específico
if len(conc_umid.dims) > 1:
    # Seleciona o ponto mais próximo da lat/lon desejada
    serie_temporal = conc_umid.sel(lat=-23.5, lon=-46.6, method="nearest")
else:
    serie_temporal = conc_umid

# 3. Plota o gráfico de linha
plt.figure(figsize=(10, 5))
serie_temporal.plot(marker="o", color="blue")
plt.title("Variação da Concentração ao Longo do Tempo")
plt.grid(True)

plt.show()