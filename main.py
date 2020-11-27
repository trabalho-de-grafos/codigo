from src import arquivo
from src import aluno
from src import grupo



if __name__ == '__main__':

    # numero de professores = k
    num_professores = 3

    arquivo1 = arquivo.input('aluno.txt')
    alunos = []
    alunos_relations = []
    grupos = []
    dissimilar_array = []


    for line in arquivo1:
        alunos.append(aluno.Aluno(line[0], line[1]))



    arquivo2 = arquivo.input('matrix.txt')


    # definir as dissimilaridades aceitas nos grupos
    for line in arquivo2:
        for num in line:
            if num!=0 and num not in dissimilar_array:
                dissimilar_array.append(num)
    dissimilar_array.sort()

    array_group = []

    # Para 3 grupos
    array_group.append(dissimilar_array[0])
    array_group.append(dissimilar_array[1])
    array_group.append(dissimilar_array[2])



    # aluno n
    for aluno in alunos:
        # percorrer matriz
        # i é a linha, line é um vetor.
        for i, line in enumerate(arquivo2):
            # j é a posição no vetor line e num é o conteúdo na posição
            for j, num in enumerate(line):
                # filtros referentes ao codigo da area e indice de dissimilaridade
                if j!=0 and i!=0 and i!=j and aluno.cod_area==i:
                    # retorna todos resultados - proximo if filtra
                    if num in array_group:
                        # print(aluno.cod_aluno, aluno.cod_area, i, j, num)
                        alunos_relations.append([aluno.cod_aluno, aluno.cod_area, j, num])
                        # print(alunos_relations)
            if alunos_relations != []:
                grupos.append(alunos_relations)
            alunos_relations = []


    # Grupos genéricos formados
    # grupo[0] = cod_aluno
    # grupo[1] = cod_area
    # grupo[2] = cod_outra_area
    # grupo[3] = dissimilaridade

    # formar os grupos finais
    grupo1 = []
    grupo2 = []
    grupo3 = []

    #alunos com grupo
    lista_reservada = []

    for gru in grupos:
        # print(gru)
        for mini_gru in gru:
            if array_group[2] == mini_gru[3] and mini_gru[0] not in lista_reservada:
                grupo1.append(mini_gru)
                lista_reservada.append(mini_gru[0])
            elif array_group[1] == mini_gru[3] and mini_gru[0] not in lista_reservada:
                grupo2.append(mini_gru)
                lista_reservada.append(mini_gru[0])
            elif array_group[0] == mini_gru[3] and mini_gru[0] not in lista_reservada:
                grupo3.append(mini_gru)
                lista_reservada.append(mini_gru[0])


    print(grupo1)
    print(grupo2)
    print(grupo3)








