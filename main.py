from src import arquivo
from src import aluno
from src import grupo



if __name__ == '__main__':

    num_professores= int(input('Insert k -> numero de professores: '))
    simi = int(input('Insira a dissimilaridade minima: '))
    arquivo1 = arquivo.input('aluno.txt')
    alunos = []
    grupos = []
    print(arquivo1)


    for line in arquivo1:
        alunos.append(aluno.Aluno(line[0], line[1]))



    arquivo2 = arquivo.input('matrix.txt')


    # navegar matriz
    for line in arquivo2:
        for num in line:
            print(num)












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
