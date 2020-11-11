from src import arquivo
from src import aluno
from src import grupo



if __name__ == '__main__':

    num_professores= int(input('Insert k -> numero de professores: '))
    arquivo1 = arquivo.input('aluno.txt')
    alunos = []
    grupos = []
    print(arquivo1)


    for line in arquivo1:
        alunos.append(aluno.Aluno(line[0], line[1]))


    # for al in alunos:
    #     al.cod_aluno, al.cod_area


    arquivo2 = arquivo.input('matrix.txt')

    similar_array = []
    similar_aux_dict = {}

    for line in arquivo2:
        for num in line:
            similar_array.append(num)
    print(" similar: ", similar_array)

    # selecionando a similaridade baseada em k grupos
    for num in similar_array:
        if num !=0 and num not in similar_aux_dict.keys():
            similar_aux_dict[num] = similar_array.count(num)

    print(similar_aux_dict)

    aluno_similar_to = {}

    for aluno in alunos:
        for i, line in enumerate(arquivo2):
            for j, column in enumerate(line):
                aluno_similar_to[aluno.cod_area] = grupo.detecta_area_similar(aluno.cod_area, j, column, similar_aux_dict.values())

