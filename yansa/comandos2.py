import subprocess

# 1. Executar um comando simples (sem capturar saída)
# subprocess.run(["ls", "-l"])

# 2. Executar comando e capturar a saída (stdout)
resultado = subprocess.run(["wc", "-l", "<", "fm0209.csv"], capture_output=True, text=True)
print(resultado.stdout)

# 3. Executar com tratamento de erro (gera exceção se falhar)
# try:
#     subprocess.run(["ls", "/pasta/que/nao/existe"], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Erro: {e}")
