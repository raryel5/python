import xarray as xr

# 1. Abrir o dataset
ds = xr.open_dataset('maoaafcpcF1.b1.20140222.143709.nc')

# 2. Ver as variáveis disponíveis
print(ds)

# 3. Ler uma variável específica (ex: temperatura 'tas')
temperatura = ds['concentration']

# 4. Converter em array do NumPy ou DataFrame do Pandas
array_np = temperatura.values
df_pandas = temperatura.to_dataframe()