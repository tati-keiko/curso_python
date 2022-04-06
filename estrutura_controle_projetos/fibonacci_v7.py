# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(int(input('Quantos números você quer\
 visualizar da sequência de Fibonacci? '))):
        print(fib)
