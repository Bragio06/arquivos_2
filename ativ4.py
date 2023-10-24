def procurarAluno():

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt', 'r') as arquivo:
        escolha_aluno = input("Qual aluno deseja procurar: ")
        
        for linha in arquivo:

            if escolha_aluno in linha:
                print(linha)
                return linha