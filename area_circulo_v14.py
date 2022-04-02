from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help(): 
    print("É necessário informar o raio do círculo.")
    print("O raio deve ser maior que zero")
    print(f"Sintaxe: python {sys.argv[0]} <raio>")

def isNumber(test: str) -> bool:
    try:
        float(test) 
        return True
    except ValueError:
        return False

def numberAndGreaterThanZero(condition: bool, num: str) -> bool:
    if condition:
        num = float(num)
        if num > 0:
            return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    test = isNumber(sys.argv[1])

    if not numberAndGreaterThanZero(test, sys.argv[1]):
        help()
        print(TerminalColor.ERRO +
              'O raio deve ser uma valor numérico.' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)


    raio = sys.argv[1]
    area = circulo(raio)
    print(f'A área do círculo é de {area} cm2.')
