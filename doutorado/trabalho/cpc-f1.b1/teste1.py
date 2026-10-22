import netCDF4 as nc

# 1. Abrir o arquivo NetCDF
ds = nc.Dataset('maoaafcpcF1.b1.20140222.143709.nc', 'r')

# 2. Listar as variáveis do arquivo
print(ds.variables.keys())

# 3. Ler os dados de uma variável específica
# [:] carrega todos os dados da variável para a memória
variavel_dados = ds.variables['concentration'][:]

# 4. Fechar o arquivo após o uso
ds.close()