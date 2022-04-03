# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')

# Função sortear_dado numeros entre 1 e 6
# for com range de 1 a 6
# se for impar continue
# se o numero for par e for igual ao valor sorteado pela
# função dado imprimir "ACERTOU" e depois chamar o break
# se não acertar chamar o else... print('Não acertou o número)

from random import randint


def sortear_dado():
    return randint(1, 6)


for numero in range(1, 7):
    if numero % 2 == 1:
        continue

    if numero == sortear_dado():
        print(f"ACERTOU! O número era {numero}")
        break
else:
    print(f'Não acertou, o número era {numero}')
