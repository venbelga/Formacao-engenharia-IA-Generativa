numeros = [10, 20, 30, 40, 50]
nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

print('Primeiro número:', numeros[0])
print('Primeiro nome:', nomes[0])
print('Último número:', numeros[-1])
print('Último nome:', nomes[-1])

print('Modificando primeiro número para 15')
numeros[0] = 15
print('Número modificado:', numeros[0]) 
print('Modificando primeiro nome para "Alex"')
nomes[0] = "Alex"
print('Nome modificado:', nomes[0])
print('Tamanho da lista de números:', len(numeros))
print('Tamanho da lista de nomes:', len(nomes))

print('Tamanho da lista de números:', len(numeros))
print('Tamanho da lista de nomes:', len(nomes))

print('Removendo o último número')
numeros.pop()
print('Lista de números após remoção:', numeros)   
print('Removendo o primeiro nome')
nomes.pop(0)
print('Lista de nomes após remoção:', nomes)