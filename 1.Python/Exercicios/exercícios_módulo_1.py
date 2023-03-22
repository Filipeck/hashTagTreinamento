"""# Exercícios do Módulo 1 - Operações, Variáveis e Input

### Parte 1 - Operações e Variáveis
Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 150<br>
Quantidade de Vendas de Pepsi = 130<br>
Preço Unitário da Coca = 1,50 <br>
Preço Unitário da Pepsi = 1,50<br>
Custo da Loja: 2.500,00

Use o bloco abaixo para criar todas as variáveis que precisar.
"""
qtdade_coca = 150
preco_coca = 1.5
qtdade_pepsi = 130
preco_pepsi = 1.5
custo = 2500
faturamento = qtdade_pepsi * preco_pepsi + qtdade_coca * preco_coca
lucro = faturamento - custo

"""1. Qual foi o faturamento de Pepsi da Loja?"""
print(f'O faturamento de Pepsi foi de \033[31mR${qtdade_pepsi * preco_pepsi}\033[m')

"""2. Qual foi o faturamento de Coca da Loja?"""
print(f'O faturamento de Coca foi de \033[31mR${qtdade_coca * preco_coca}\033[m')

"""3. Qual foi o Lucro da loja?"""
print(f'O lucro da loja é de \033[31mR${lucro}\033[m')

"""4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual"""
print(f'A margem da loja foi de \033[31mR${lucro / faturamento:.2f}%\033[m')
"""### Parte 2 - Inputs e Strings

A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 
1.000 produtos e possui um código para cada produto.
Ex: 
Coca -> Código: BEB1300543<br>
Pepsi -> Código: BEB1300545<br>
Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
Vodka Smirnoff -> Código: BAC17675002<br>

Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do 
código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa 
deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
"""
print('=' * 30)
print(f'{"A bebida é alcóolica?":^30}')
print('=' * 30)
alcoolica = str(input('Por favor, insira o código da bebida: '))
teste = ('BAC' in alcoolica or 'bac' in alcoolica)
if teste:
    print('A bebida é alcóolica!')
else:
    print('A bebida não é alcóolica!')
