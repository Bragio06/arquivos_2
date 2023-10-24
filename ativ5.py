import ast

def removerEstudante():

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt', 'r') as arquivo:
        escolha_aluno = input("Qual aluno deseja remover: ")

        for linha in arquivo: 
            linha = ast.literal_eval(linha)

            if escolha_aluno in linha:
                linha = {}
                
                print(linha)