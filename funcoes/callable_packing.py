def calc_preco_final(preco_bruto, calc_imposto, *params):
    return preco_bruto + preco_bruto * calc_imposto(*params)


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, True)
    preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
    print(f'Preço final: R${preco_final}')


# exemplo que faz mais sentido:
def calc_preco_final2(calc_imposto2, *params2):
    return calc_imposto2(*params2)


def imposto_x2(importado):
    return 0.22 if importado else 0.13


def imposto_y2(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto2 = 134.98
    preco_final2 = \
        preco_bruto2+preco_bruto2*(calc_preco_final2(imposto_x, True) +
                                   calc_preco_final2(imposto_y, True, 1.5))
    print(f'Preço final: R${preco_final2}')
