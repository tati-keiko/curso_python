from math import pi


def circulo(raio):
    print('A área do círculo é de', pi * float(raio) ** 2, 'cm2.')


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
