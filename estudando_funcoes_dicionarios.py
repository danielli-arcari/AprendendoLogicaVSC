# Estudando métodos e funções em listas:
lista = [1, 3, 12, 8, 2]

# append: adiciona um elemento ao final da lista
print('Antes do append: - estudando_funcoes_dicionarios.py:5', lista)
lista.append(3)
print('Depois do append: - estudando_funcoes_dicionarios.py:7', lista)

# insert: encaixando um elemento numa posição
lista.insert(2, 10)
print('Depois do insert: - estudando_funcoes_dicionarios.py:11', lista)

# extend: para juntar listas
lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend: - estudando_funcoes_dicionarios.py:16', lista)

# pop: para remover elementos
lista.pop()
print('Lista após o pop: - estudando_funcoes_dicionarios.py:20', lista)
lista.pop(0)
print('Lista após o pop(0): - estudando_funcoes_dicionarios.py:22', lista)

# remove: remove o elemento (não o índice)
lista.remove(3)
print('Depois do remove: - estudando_funcoes_dicionarios.py:26', lista)

# count: conta quantas vezes o elemento aparece
print('Quantidade de número 2 na lista: - estudando_funcoes_dicionarios.py:29', lista.count(2))

# index: retorna o índice de um elemento
print('Índice do número 12 na lista: - estudando_funcoes_dicionarios.py:32', lista.index(12))

# sort: ordena a lista
lista.sort()
print('Lista ordenada (crescente): - estudando_funcoes_dicionarios.py:36', lista)

# ordenação decrescente
lista.sort(reverse=True)
print('Lista ordenada (decrescente): - estudando_funcoes_dicionarios.py:40', lista)

# FUNÇÕES PARA LISTAS:
print('Quantidade de elementos na lista: - estudando_funcoes_dicionarios.py:43', len(lista))
print('Soma dos elementos da lista: - estudando_funcoes_dicionarios.py:44', sum(lista))
print('Maior valor da lista: - estudando_funcoes_dicionarios.py:45', max(lista))
print('Menor valor da lista: - estudando_funcoes_dicionarios.py:46', min(lista))

# 2 - CRIAÇÃO DE FUNÇÕES:
# função inicial
def saudacao_inicial():
    print('Seja bemvindo(a)! - estudando_funcoes_dicionarios.py:51')
    print('Olá, é um prazer ter você fazendo parte desse curso! - estudando_funcoes_dicionarios.py:52')

saudacao_inicial()

# função com parâmetros
def saudacao(nome, curso):
    print(f'Seja bemvindo(a), {nome}! - estudando_funcoes_dicionarios.py:58')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}! - estudando_funcoes_dicionarios.py:59')

saudacao('Walisson', 'Python')
saudacao('Aline', 'Java')

# função com parâmetro default
def saudacao_padrao(nome, curso='Python'):
    print(f'Seja bemvindo(a), {nome}! - estudando_funcoes_dicionarios.py:66')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}! - estudando_funcoes_dicionarios.py:67')

saudacao_padrao('Walisson', 'C++')
saudacao_padrao('Joana')  # exemplo com valor padrão

# funções com retorno
def soma_exibe(num1, num2):
    print('Soma = - estudando_funcoes_dicionarios.py:74', num1 + num2)

soma_exibe(5, 7)

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é: - estudando_funcoes_dicionarios.py:82', resultado)

# Outro exemplo:
def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    else:
        return 'Operação inválida'

resultado = calculadora(10, 20)
print(resultado)

# DICIONÁRIOS:
# Criando dicionário
dicionario = {}  # ou dicionario = dict()
dicionario = {'nome': 'Walisson', 'idade': 26, 'altura': 1.77}
print(dicionario)
print('Idade: - estudando_funcoes_dicionarios.py:101', dicionario['idade'])

# adicionando elementos
dicionario['programador'] = True
print(dicionario)

# Iterando
for variavel in dicionario:
    print(variavel, dicionario[variavel])

# testando existência de chaves
print('peso - estudando_funcoes_dicionarios.py:112' in dicionario)
print('altura - estudando_funcoes_dicionarios.py:113' in dicionario)
             