equipamentos = {
    'parafusos com bucha 6 mm':9,
    'arruelas para os parafusos de 6 mm':6,
    'abraçadeiras de 1 polegada':4,
    'parafuso sextavado de 6 mm de diâmetro e 3 cm de comprimento':2,
    'porca para parafuso sextavado de 6 mm': 2,
    'arruela para parafuso sextavado de 6 mm':2,
    'caixa CFTV':1,
    'kit raspberry pi 4':1,
    'eletroduto galvanizado de 1 polegada e 1,5 m (no comércio só vendem o de 3 m)':1,
    'prensa cab PG-11 p/ cabos 6-10mm':1,
    'botão liga/desliga 10 A':1,
    'plug macho para tomada 10 A':1,
    'conector borne sindal 4 mm':2,
    'conector Borne Sindal 10 mm':2
}

option = int(input('Escolha uma opção: \n' \
'0 calcular lista de compras\n'
'1 inserir um novo item\n'
'2 cadastrar nova categoria\n'
'3 excluir um item\n' \
'\n'
'Digite a opção desejada: '))

if option == 0:
    nKits = int(input('Quantos kits serão montados? '))

    listaCompras = {}

    for chave, valor in equipamentos.items():
        listaCompras[chave] = valor * nKits

    print(listaCompras)

with open('compras.txt', 'w', encoding='utf-8') as arquivo:
    for chave, valor in listaCompras.items():
        arquivo.write(f'{valor}x : {chave}\n')