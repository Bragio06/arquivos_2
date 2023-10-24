import ast

def contarCursos():
    cursos = []

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = ast.literal_eval(linha)

            cursos.append(linha['curso'])
        
        i = 0

        for items in cursos:
            contagem = cursos.count(cursos[i])
            print(f"{items} = {contagem}")

            i += 1

    return cursos