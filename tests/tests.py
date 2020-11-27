
import unittest
from src import arquivo
from src import aluno
from src import grupo


def  test_Area_Aluno(cod_area):
    if not len(cod_area) == 1:
        print("esta certo")

    #self.assertEqual(var.cod_area,next(var.cod_area),"esse ")


class MyTestCase(unittest.TestCase):
    #def test_something(self):
        #self.assertEqual(True, False)

    def test_Area_Aluno(self,*cod_area):
        if  len(cod_area) == 1:
             print("esta certo")
             return True



    def test_guant_grupo(self, num_professores =int, grupos =int):
        self.assertEqual(num_professores, grupos,True)



    def test_Grau_Dissimimiliaridade(self, *dissimilar_array,arquivo,cod_area=int,cod_area2=int,):
        for i, line in enumerate(arquivo):
            for j, num in enumerate(line):
                if j != 0 and i != 0 and i != j and cod_area == i:
                    if j != 0 and i != 0 and i != j and cod_area2 == j:
                        self.assertEqual(dissimilar_array[cod_area2],dissimilar_array[cod_area],True)

         #for x, in len(*lst):
            # self.assertEqual(lst[x],dissimilar_array[x],"deu certo")









if __name__ == '__main__':
    unittest.main()


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


    # Imprimir Grupos de pesquisa
    print('Grupo 1: ')
    for gr in grupo1:
        print('Código Aluno: ', gr[0], 'Área Pesquisa',gr[1])

    print('Grupo 2: ')
    for gr in grupo2:
        print('Código Aluno: ', gr[0], 'Área Pesquisa',gr[1])

    print('Grupo 3: ')
    for gr in grupo3:
        print('Código Aluno: ', gr[0], 'Área Pesquisa',gr[1])

    test_Area_Aluno(aluno.cod_area)

    test_guant_grupo(num_professores,len(grupos))

    test_Grau_Dissimimiliaridade(arquivo2,dissimilar_array,aluno.cod_area,aluno.cod_area)


