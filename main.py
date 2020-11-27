from src import arquivo
from src import aluno
from src import grupo



if __name__ == '__main__':

    #num_professores= int(input('Insert k -> numero de professores: '))
    num_professores = 3
    # simi = int(input('Insira a dissimilaridade minima: '))
    simi = 50
    arquivo1 = arquivo.input('aluno.txt')
    alunos = []
    alunos_relations = []
    grupos = []
    grupos_finais = []
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
                        alunos_relations.append([aluno.cod_aluno, aluno.cod_area, j])
                        # print(alunos_relations)
            if alunos_relations != []:
                grupos.append(alunos_relations)
            alunos_relations = []


    # Grupos genéricos formados
    # grupo[0] = cod_aluno
    # grupo[1] = cod_area
    # grupo[2] = cod_outra_area
    for gru in grupos:
        for mini_gru in gru:
            print(mini_gru)






















                # if aluno.cod_area == i and aluno.cod_area != j:
                #     # pegar o conteudo num de line.
                #
                #     if num > simi:
                #         print('aluno:', aluno.cod_aluno, ' cod_area: ', j,' similaridade: ', num)

                       # print(aluno.cod_aluno,' similaridade: ', num)

                    # if aluno.cod_area > simi:
                    #     for alun2 in alunos:
                    #         if alun2.cod_aluno != aluno.cod_aluno:
                    #             if alun2.cod_area == j:

                                    # arquivo2[i][j]









    # navegar matriz













    #         similar_array.append(num)
    # print(" similar: ", similar_array)
    #
    # # selecionando a similaridade baseada em k grupos
    # for num in similar_array:
    #     if num !=0 and num not in similar_aux_dict.keys():
    #         similar_aux_dict[num] = similar_array.count(num)/2
    #
    # print(similar_aux_dict)


    # Percorrer similaridade e pegar k grup



    # aluno_similar_to = {}
    #
    # for aluno in alunos:
    #     for i, line in enumerate(arquivo2):
    #         for j, column in enumerate(line):
    #             aluno_similar_to[aluno.cod_area] = grupo.detecta_area_similar(aluno.cod_area, j, column, similar_aux_dict.values())
    #
