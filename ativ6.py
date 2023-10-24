import ast

def calcularIdadeMedia():
    soma = 0
    quantidade = 0
    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt', 'r') as arquivo:
        for linha in arquivo:

            linha = ast.literal_eval(linha)
            soma = soma + linha['idade']
            quantidade += 1

        media = soma / quantidade

    return media