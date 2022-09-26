frase = input('Digite uma frase: ').upper().strip()
print('Quantidade de "A" na frase: ', frase.count('A'))
print('Primeira vez que aparece: ', frase.find('A') + 1)
print('Ultima vez que aparece: ', frase.rfind('A') + 1)
