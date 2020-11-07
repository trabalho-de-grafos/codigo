
def input(filename):
    arq = open('files/input/'+filename, 'r')
    input_line_list = arq.readlines()
    arq.close()
    formmated = []

    for line in input_line_list:
        no_paragraph_line = line.replace('\n','')
        no_paragraph_line = no_paragraph_line.split()
        line = no_paragraph_line
        number_line = []

        for str in line:
            number_line.append( int(str))

        formmated.append(number_line)

    return formmated


def output(text, filename):
    # Em implementação
    path = '../files/output/'+filename
    arq = open(path, 'w')
    arq.write(text)
    arq.close()
    return print('Sucesso ao escrever arquivo')

