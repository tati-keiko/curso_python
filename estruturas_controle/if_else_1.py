nota_aluno = input('Informe a nota do aluno: ')
nota = float(nota_aluno)


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


if __name__ == "__main__":

    if nota >= 9 and nota <= 10:
        print("A")
    elif nota >= 8 and nota < 9:
        print("A-")
    elif nota >= 7 and nota < 8:
        print("B")
    elif nota >= 6 and nota < 7:
        print("B-")
    elif nota >= 5 and nota < 6:
        print("C")
    elif nota >= 4 and nota < 5:
        print("C-")
    elif nota >= 3 and nota < 4:
        print("D")
    elif nota >= 2 and nota < 3:
        print("D-")
    elif nota >= 1 and nota < 2:
        print("E")
    elif nota >= 0 and nota < 1:
        print("E-")
    else:
        print(TerminalColor.ERRO + "Nota inválida" + TerminalColor.NORMAL)
