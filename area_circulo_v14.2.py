from math import pi
import sys
import errno


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: python {sys.argv[0]} <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser uma valor numérico.')
        sys.exit(errno.EINVAL)

raio = sys.argv[1]
area = circulo(raio)
print(f'A área do círculo é de {area} cm2.')
