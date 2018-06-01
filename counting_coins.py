import time


valor_unidade_moeda = [5, 10, 25, 50, 100]
tamanho = len(valor_unidade_moeda)


def conta_minimo_de_moedas(valor):
    resultado = []

    for atual in range(tamanho-1, 0, -1):
        while(valor >= valor_unidade_moeda[atual]):
            valor -= valor_unidade_moeda[atual]
            resultado.append(valor_unidade_moeda[atual])

    print(resultado)


def main():
    valor_total = 85

    print("\nPara o valor", valor_total, "o numero minimo de moedas eh:\n")

    inicio = time.time()
    conta_minimo_de_moedas(valor_total)
    fim = time.time()

    print('\nTempo para execucao: ', fim-inicio)

if __name__ == '__main__':
    main()
