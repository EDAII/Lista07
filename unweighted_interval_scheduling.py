import time
from datetime import datetime


class Atividade(object):

    def __init__(self, nome, inicio, fim):
        self.nome = nome
        # d = dia, b = mes, Y = ano, H = horas
        self.inicio = int(time.mktime(datetime.strptime(
                                    inicio, "%d de %b de %Y").timetuple()))
        self.fim = int(time.mktime(datetime.strptime(
                                    fim, "%d de %b de %Y").timetuple()))

    def __repr__(self):
        return str((self.nome, self.inicio, self.fim))


def seleciona_atividades(atividades):

    # Ordena pelas atividades com menor duracao
    atividades.sort(lambda x, y: x.fim - y.inicio)

    cronograma = []
    fim = 0

    for atividade in atividades:
        if fim <= atividade.inicio:
            fim = atividade.fim
            cronograma.append(atividade)

    return cronograma

if __name__ == '__main__':

    atividades = []

    atividades.append(Atividade("Trabalho extra", "2 de Jan de 2018", "3 de Feb de 2018"))
    atividades.append(Atividade("Trabalho em grupo", "2 de Jan de 2018", "1 de Feb de 2018"))
    atividades.append(Atividade("Trabalho em dupla", "6 de May de 2018", "1 de Jun de 2018"))
    atividades.append(Atividade("Trabalho Final", "3 de Feb de 2018", "5 de Feb de 2018"))
    atividades.append(Atividade("Trabalho pratico", "5 de Feb de 2018", "6 de Jun de 2018"))

    inicio = time.time()
    cronograma = seleciona_atividades(atividades)
    fim = time.time()

    print("Tempo para execucao: ", fim-inicio)

    for i in range(len(cronograma)):
        print (cronograma[i].nome + "\n")
