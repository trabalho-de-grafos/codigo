# Trabalho Prático de Grafos

a) **Contexto do trabalho:** Pontifícia Universidade Católica de Minas Gerais. 

**Curso:** Engenharia de Software/Noturno. 

**Disciplina:** Algoritmos Computacionais em Grafos. **Professora:** Joyce Christina de Paiva Carvalho. 

**Alunos:** Daniel Henrique Rodrigues Costa, Geovane de Freitas Queiroz Morcatti, Guilherme Henrique Ladislau Biagini & Weber Marques de Oliveira

---------------------------------------------------------------------------------------------------------------------------------
 
b) **Desenvolvedores:** Daniel Henrique Rodrigues Costa, Geovane de Freitas Queiroz Morcatti, Guilherme Henrique Ladislau Biagini & Weber Marques de Oliveira

---------------------------------------------------------------------------------------------------------------------------------
 
c) **Dependências** O trabalho foi feito na linguagem Python na IDE Visual Studio Code implementando as funções linting, debug, execução, testes, etc.; utilizamos esse vídeo para a configuração da IDE (https://www.youtube.com/watch?v=ZQ60SJDACuc).

---------------------------------------------------------------------------------------------------------------------------------

d) **Licenciamento:GPLv3** Créditos : https://github.com/trabalho-de-grafos

---------------------------------------------------------------------------------------------------------------------------------


<h1> Algumas classes e pacotes que utilizamos: </h1>

<ol>
Pacote src:
Classe Aluno: Possui um construtor aluno.
Classe Grupo: Checa a similaridade dos grupos.
Classe Arquivo: Operações de arquivo (ler, escrever, gravar, procurar, ect.).
Pacote test:
Classe tests: Possui 3 casos de testes
test_Area_Aluno: verifica se o aluno possui uma área de pesquisa ou está associado á mais de uma.
test_Grau_dissimilaridade: verifica se a similaridade é a mesma do que a digitada.
test_quant_Grupos: verifica se os números de grupos é igual ao número de professores. 

Pacote files 
Pacote input: Armazena os arquivos dos alunos e professores de entrada.
Pacote output : Armazena o arquivo de saída.

Classe main: Ponto de início de execução da aplicação.
</ol>
```

---------------------------------------------------------------------------------------------------------------------------------

<h1> Sobre o programa: </h1>
<p align="justify"> A lógica da solução se baseia em receber um arquivo TXT de aluno que gera um objeto aluno e depois tem um segundo arquivo de uma matriz que é percorrido e mapeia a similaridade, essa similaridade é uma matriz que liga o código das áreas x código das outras áreas e é baseada em uma interseção de uma área e de outra área, com essa interseção conseguimos mapear a similaridade para a quantidade de grupos separando os alunos por grupos, depois de formar os grupos alocamos 1 professor para cada grupo resolvendo o problema descrito no trabalho.</p>



--------------------------------------------------------------------------------------------------------------------------------------
